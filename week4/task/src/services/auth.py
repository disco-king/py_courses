from datetime import datetime, timedelta
import uuid

from passlib.hash import bcrypt
from sqlmodel import Session
from jose import jwt, JWTError, ExpiredSignatureError
from fastapi import HTTPException, Depends, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.db import AbstractCache, get_cache, get_session
from src.services import ServiceMixin
from src.services.store import StoreService, get_store_service
from src.models.user import User
from src.api.v1.schemas import UserModel, UserCreate, Token
from src.core.config import JWT_ALGORITHM, JWT_SECRET_KEY
from src.core.config import JWT_EXPIRATION_TIME, JWT_REFRESH_TIME

__all__ = (
    "AuthService",
    "get_auth_service",
    "get_refresh_uuid",
    "get_access",
    "get_access_and_invalidate",
)

common_status = status.HTTP_401_UNAUTHORIZED

bearer = HTTPBearer()


def decode_and_check(
    credentials: str,
    store_service: StoreService
) -> dict:
    token_content = AuthService.validate_token(credentials)
    if store_service.token_in_blacklist(token_content["jti"]):
        raise HTTPException(status_code=common_status, detail="Token is blacklisted")
    return token_content


def get_access(
    creds: HTTPAuthorizationCredentials = Security(bearer),
    store_service: StoreService = Depends(get_store_service)
) -> UserModel:
    token_content = decode_and_check(creds.credentials, store_service)
    return UserModel.parse_obj(token_content)


def get_access_and_invalidate(
    creds: HTTPAuthorizationCredentials = Security(bearer),
    store_service: StoreService = Depends(get_store_service)
) -> UserModel:
    token_content = decode_and_check(creds.credentials, store_service)
    store_service.store_access_token(token_content["jti"])
    store_service.delete_refresh_token(
        token_content["uuid"],
        token_content["refresh_uuid"],
    )
    return UserModel.parse_obj(token_content)


def get_refresh_uuid(
    creds: HTTPAuthorizationCredentials = Security(bearer),
    store_service: StoreService = Depends(get_store_service)
) -> str:
    token_content = AuthService.validate_refresh(creds.credentials)
    if not store_service.token_in_whitelist(token_content["uuid"], token_content["jti"]):
        raise HTTPException(status_code=common_status, detail="Token is blacklisted")
    return token_content["uuid"]


class AuthService(ServiceMixin):

    @classmethod
    def verify_pswd(cls, plain_pswd: str, hashed_pswd: str) -> bool:
        return bcrypt.verify(plain_pswd, hashed_pswd)

    @classmethod
    def hash_pswd(cls, plain_pswd: str) -> str:
        return bcrypt.hash(plain_pswd)

    @classmethod
    def decode_token(cls, token: str, tok_type: str) -> dict:
        try:
            payload = jwt.decode(
                token,
                JWT_SECRET_KEY,
                algorithms=[JWT_ALGORITHM]
            )

        except ExpiredSignatureError:
            raise HTTPException(status_code=common_status, detail="Token has expired")

        except JWTError:
            raise HTTPException(status_code=common_status, detail="Token is invalid")

        if payload["type"] != tok_type:
            raise HTTPException(status_code=common_status, detail="Token type error")
        return payload


    @classmethod
    def validate_token(cls, token: str) -> dict:
        payload = cls.decode_token(token, "access")
        return payload


    @classmethod
    def validate_refresh(cls, token: str) -> dict:
        payload = cls.decode_token(token, "refresh")
        return payload


    @classmethod
    def create_payload(cls, tok_type: str, user_uuid: str) -> dict:
        now = datetime.utcnow()
        if tok_type == "access":
            delta = timedelta(minutes=int(JWT_EXPIRATION_TIME))
        else:
            delta = timedelta(days=int(JWT_REFRESH_TIME))

        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + delta,
            "jti": str(uuid.uuid4()),
            "uuid": user_uuid,
            "type": tok_type
        }
        return payload

    @classmethod
    def create_token(
        cls,
        user: UserModel,
        store_service: StoreService
    ) -> Token:

        access_payload = cls.create_payload("access", user.uuid)
        refresh_payload = cls.create_payload("refresh", user.uuid)

        for key, value in user.dict().items():
            if key == "password_hash":
                continue
            if isinstance(value, datetime):
                access_payload[key] = int(value.timestamp())
            else:
                access_payload[key] = value

        access_payload["refresh_uuid"] = refresh_payload["jti"]
        store_service.store_refresh_token(refresh_payload["uuid"], refresh_payload["jti"])

        access_token = jwt.encode(
            access_payload,
            JWT_SECRET_KEY,
            algorithm=JWT_ALGORITHM
        )

        refresh_token = jwt.encode(
            refresh_payload,
            JWT_SECRET_KEY,
            algorithm=JWT_ALGORITHM
        )

        return Token(access_token=access_token, refresh_token=refresh_token)


    def authenticate(
        self,
        username: str,
        password: str,
        store_service: StoreService
    ) -> Token:
        exception = HTTPException(
                        status_code=common_status,
                        detail="Incorrect username or password"
                    )
        
        user = self.session.query(User).filter(User.username == username).first()

        if not user:
            raise exception

        if not self.verify_pswd(password, user.password_hash):
            raise exception

        return self.create_token(user, store_service)


def get_auth_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> AuthService:
    return AuthService(cache=cache, session=session)