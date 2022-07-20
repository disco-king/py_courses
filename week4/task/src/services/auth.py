from datetime import datetime, timedelta

from passlib.hash import bcrypt
from sqlmodel import Session
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError

from src.db import AbstractCache, get_cache, get_session
from src.services import ServiceMixin
from src.services import UserService, get_user_service
from src.models.user import User
from src.api.v1.schemas import UserModel, UserCreate, Token
from src.core.config import JWT_ALGORITHM
from src.core.config import JWT_SECRET_KEY
from src.core.config import JWT_EXPIRATION_TIME

__all__ = (
    "AuthService",
    "get_current_user",
    "get_auth_service"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    return AuthService.validate_token(token)


class AuthService(ServiceMixin):

    @classmethod
    def verify_pswd(cls, plain_pswd: str, hashed_pswd: str) -> bool:
        return bcrypt.verify(plain_pswd, hashed_pswd)

    @classmethod
    def hash_pswd(cls, plain_pswd: str) -> str:
        return bcrypt.hash(plain_pswd)

    @classmethod
    def validate_token(cls, token: str) -> UserModel:
        exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid credentials"
            )
        try:
            payload = jwt.decode(
                token,
                JWT_SECRET_KEY,
                algorithms=[JWT_ALGORITHM]
            )
        except JWTError:
            raise exception
        
        user = UserModel.parse_obj(payload)

        return user

    @classmethod
    def create_token(cls, user: User) -> Token:

        now = datetime.utcnow()

        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(minutes=int(JWT_EXPIRATION_TIME)),
            # "sub": user.username,
        }

        for key, value in user.dict().items():
            if key == "password_hash":
                continue
            if isinstance(value, datetime):
                payload[key] = str(value)
            else:
                payload[key] = value

        token = jwt.encode(
            payload,
            JWT_SECRET_KEY,
            algorithm=JWT_ALGORITHM
        )

        return Token(access_token=token)

    # def __init__(self, session: Session = Depends(get_session)):
    #     self.session = session


    def authenticate(self, username: str, password: str) -> Token:
        exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="incorrect username or password"
            )
        
        user = self.session.query(User).filter(User.username == username).first()
        
        if not user:
            raise exception

        if not self.verify_pswd(password, user.password_hash):
            raise exception

        return self.create_token(user)

def get_auth_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> AuthService:
    return AuthService(cache=cache, session=session)