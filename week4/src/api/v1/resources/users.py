from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError

from src.api.v1.schemas import UserUpdate, UserModel, Token
from src.services import AuthService, get_auth_service 
from src.services import UserService, get_user_service
from src.services import StoreService, get_store_service
from src.services import get_access, get_access_and_invalidate

router = APIRouter()


@router.get(
    path="/me",
    response_model=UserModel,
    summary="Посмотреть свой профиль",
    tags=["users"],
)
def user_detail(
    current_user: UserModel = Depends(get_access)
) -> UserModel:
    return current_user


@router.patch(
    path="/me",
    summary="Обновить свой профиль",
    tags=["users"]
)
def user_update(
    new_data: UserUpdate,
    current_user: UserModel = Depends(get_access_and_invalidate),
    user_service: UserService = Depends(get_user_service),
    auth_service: AuthService = Depends(get_auth_service),
    store_service: StoreService = Depends(get_store_service)
) -> dict:
    current_data = user_service.get_user_detail(current_user.uuid)
    if not current_data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    current_data.update(new_data.dict(exclude_unset=True))
    try:
        ret_user = user_service.update_user(current_data)
    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail="User with this name or email already exists"
        )
    token: Token = auth_service.create_token(ret_user, store_service)
    return {
        "msg": "Update is successful. Please use new access token.",
        "user": UserModel(**ret_user.dict()),
        "access_token": token.access_token
    }
