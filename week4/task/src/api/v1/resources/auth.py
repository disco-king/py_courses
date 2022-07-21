from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError

from src.api.v1.schemas import UserCreate, UserModel, UserLogin, Token
from src.services import AuthService, get_auth_service
from src.services import get_refresh_uuid
from src.services import UserService, get_user_service
from src.models import User

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
def log_in(
    user_data: UserLogin,
    service: AuthService = Depends(get_auth_service),
) -> dict:
    token: Token = service.authenticate(
        user_data.username,
        user_data.password
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
    user_uuid: str = Depends(get_refresh_uuid)
) -> dict:
    user_data: dict = user_service.get_user_detail(user_uuid)
    token: Token = auth_service.create_token(User(**user_data))
    return {
        "access_token": token.access_token,
        "refresh_token": token.refresh_token
    }