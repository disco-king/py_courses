from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from src.api.v1.schemas import UserCreate, UserModel, Token
from src.services import AuthService, get_auth_service 
from src.services import UserService, get_user_service

router = APIRouter()

@router.post(
    path="/signup",
    summary="Зарегистрировать нового пользователя",
    tags=["users"],
)
def user_create(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
) -> dict:
    user: dict = user_service.create_user(user=user)
    return {"msg": "User created.", "user": UserModel(**user)}


@router.post(
    path="/login",
    response_model=Token,
    tags=["users"]
)
def log_in(
    service: AuthService = Depends(get_auth_service),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    return service.authenticate(
        form_data.username,
        form_data.password
    )