from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status

from src.models import User
from src.api.v1.schemas import UserCreate, UserModel
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
    current_user: User = Depends(get_current_user)
) -> UserModel:
    return current_user


@router.put(
    path="/me",
    tags=["users"]
)
def user_update():
    pass
