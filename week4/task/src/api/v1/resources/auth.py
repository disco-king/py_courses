from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError

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