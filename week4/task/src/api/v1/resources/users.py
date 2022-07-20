from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status

from src.api.v1.schemas import UserCreate, UserModel
from src.services import UserService, get_user_service

router = APIRouter()

@router.get(
    path="/{username}",
    response_model=UserModel,
    summary="Посмотреть чей-то профиль",
    tags=["users"],
)
def user_detail(
    username: str, user_service: UserService = Depends(get_user_service),
) -> UserModel:
    user: Optional[dict] = user_service.get_user_detail(username=username)
    if not user:
        # Если пользователь не найден, отдаём 404 статус
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="user not found")
    return UserModel(**user)



