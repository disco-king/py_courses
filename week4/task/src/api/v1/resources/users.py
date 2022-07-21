from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status

from src.models import User
from src.api.v1.schemas import UserCreate, UserUpdate, UserModel, Token
from src.services import AuthService, get_auth_service 
from src.services import UserService, get_user_service
from src.services import get_current_user

router = APIRouter()
@router.get(
    path="/me",
    response_model=UserModel,
    summary="Посмотреть свой профиль",
    tags=["users"],
)
def user_detail(
    current_user: UserModel = Depends(get_current_user)
) -> UserModel:
    return current_user


@router.patch(
    path="/me",
    summary="Обновить свой профиль",
    tags=["users"]
)
def user_update(
    new_data: UserUpdate,
    current_user: UserModel = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service),
    auth_service: AuthService = Depends(get_auth_service)
) -> dict:
    current_data = user_service.get_user_detail(current_user.uuid)
    current_data.update(new_data.dict(exclude_unset=True))

    ret_user = user_service.update_user(current_data)
    token: Token = auth_service.create_token(ret_user)
    return {
        "msg": "Update is successful. Please use new access token.",
        "user": UserModel(**ret_user.dict()),
        "access_token": token.access_token
    }
