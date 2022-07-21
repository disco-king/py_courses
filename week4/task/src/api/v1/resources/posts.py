from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status

from src.api.v1.schemas import PostCreate, PostListResponse, PostModel
from src.services import PostService, get_post_service
from src.models import User
from src.services import get_current_user

router = APIRouter()


def find_post(
    post_id: int,
    post_service: PostService
) -> dict:
    post: Optional[dict] = post_service.get_post_detail(item_id=post_id)
    if not post:
        # Если пост не найден, отдаём 404 статус
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Post not found")
    return post


@router.get(
    path="/",
    response_model=PostListResponse,
    summary="Список постов",
    tags=["posts"],
)
def post_list(
    post_service: PostService = Depends(get_post_service)
) -> PostListResponse:
    posts: dict = post_service.get_post_list()
    if not posts:
        # Если посты не найдены, отдаём 404 статус
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Posts not found")
    return PostListResponse(**posts)


@router.get(
    path="/{post_id}",
    response_model=PostModel,
    summary="Получить определенный пост",
    tags=["posts"],
)
def post_detail(
    post_id: int,
    post_service: PostService = Depends(get_post_service),
) -> PostModel:
    post: dict = find_post(post_id, post_service)
    return PostModel(**post)


@router.post(
    path="/",
    response_model=PostModel,
    summary="Создать пост",
    tags=["posts"],
)
def post_create(
    post: PostCreate,
    post_service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user)
) -> PostModel:
    author_name = current_user.username
    post: dict = post_service.create_post(post=post, author=author_name)
    return PostModel(**post)


@router.delete(
    path="/{post_id}",
    summary="Удалить пост",
    tags=["posts"],
)
def post_delete(
    post_id: int,
    post_service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user)
) -> Response:
    post: dict = find_post(post_id, post_service)
    if post["author"] != current_user.username:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid credentials"
                )
    post_service.delete_post(item_id=post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

