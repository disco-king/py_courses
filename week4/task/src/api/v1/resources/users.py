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



@router.post(
    path="/",
    response_model=UserModel,
    summary="Зарегистрировать нового пользователя",
    tags=["users"],
)
def user_create(
    user: UserCreate, user_service: UserService = Depends(get_user_service),
) -> UserModel:
    user: dict = user_service.create_user(user=user)
    return UserModel(**user)

# @router.delete(
#     path="/{post_id}",
#     summary="Удалить пост",
#     tags=["posts"],
# )
# def post_delete(
#     post_id: int, post_service: PostService = Depends(get_post_service),
# ) -> Response:
#     post_service.delete_post(item_id=post_id)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @router.get(
#     path="/",
#     response_model=PostListResponse,
#     summary="Список пользователей",
#     tags=["posts"],
# )
# def post_list(
#     post_service: PostService = Depends(get_post_service),
# ) -> PostListResponse:
#     posts: dict = post_service.get_post_list()
#     if not posts:
#         # Если пользователи не найдены, отдаём 404 статус
#         raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="posts not found")
#     return PostListResponse(**posts)