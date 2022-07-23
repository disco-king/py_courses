from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.exc import IntegrityError

from src.api.v1.schemas import UserCreate, UserModel, UserLogin, Token
from src.services import AuthService, get_auth_service, get_refresh_uuid
from src.services import get_access_and_invalidate
from src.services import StoreService, get_store_service
from src.services import UserService, get_user_service

router = APIRouter()

@router.post(
    path="/signup",
    summary="Зарегистрировать нового пользователя",
    tags=["users"],
    status_code=201
)
def user_create(
    user: UserCreate,
    response: Response,
    user_service: UserService = Depends(get_user_service)
) -> dict:
    try:
        user: dict = user_service.create_user(user=user)
    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="User with this name or email already exists"
        )

    return {"msg": "User created.", "user": UserModel(**user)}


@router.post(
    path="/login",
    tags=["users"],
    summary="Зайти в свой профиль"
)
def login(
    user_data: UserLogin,
    service: AuthService = Depends(get_auth_service),
    store_service: StoreService = Depends(get_store_service)
) -> dict:
    token: Token = service.authenticate(
        user_data.username,
        user_data.password,
        store_service
    )
    return {
        "access_token": token.access_token,
        "refresh_token": token.refresh_token
    }


@router.post(
    path="/refresh",
    tags=["users"],
    summary="Обновить токены"
)
def refresh(
    auth_service: AuthService = Depends(get_auth_service),
    user_service: UserService = Depends(get_user_service),
    user_uuid: str = Depends(get_refresh_uuid),
    store_service: StoreService = Depends(get_store_service)
) -> dict:
    user_data: dict = user_service.get_user_detail(user_uuid)
    token: Token = auth_service.create_token(UserModel(**user_data), store_service)
    return {
        "access_token": token.access_token,
        "refresh_token": token.refresh_token
    }

@router.post(
    path="/logout",
    tags=["users"],
    summary="Выйти из аккаунта"
)
def logout(
    user: UserModel = Depends(get_access_and_invalidate)
) -> dict:
    return {"msg": "You have successfully logged out."}


@router.post(
    path="/logout_all",
    tags=["users"],
    summary="Выйти со всех устройств"
)
def logout_all(
    user: UserModel = Depends(get_access_and_invalidate),
    store_service: StoreService = Depends(get_store_service)
) -> dict:
    store_service.clear_refresh_tokens(user.uuid)
    return {"msg": "You have successfully logged out from all devices."}