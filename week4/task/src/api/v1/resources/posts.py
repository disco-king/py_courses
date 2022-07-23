from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response

from src.api.v1.schemas import PostCreate, PostListResponse, PostModel, UserModel
from src.services import PostService, get_post_service
from src.services import get_access

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
    status_code=201
)
def post_create(
    post: PostCreate,
    response: Response,
    post_service: PostService = Depends(get_post_service),
    current_user: UserModel = Depends(get_access)
) -> PostModel:
    author_name = current_user.username
    author_uuid = current_user.uuid
    post: dict = post_service.create_post(
        post=post,
        author=author_name,
        author_uuid=author_uuid
    )
    return PostModel(**post)


@router.delete(
    path="/{post_id}",
    summary="Удалить пост",
    tags=["posts"],
)
def post_delete(
    post_id: int,
    post_service: PostService = Depends(get_post_service),
    current_user: UserModel = Depends(get_access)
) -> Response:
    post: dict = find_post(post_id, post_service)
    if post["author_uuid"] != current_user.uuid:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Invalid credentials"
        )
    post_service.delete_post(item_id=post_id)
    return Response(status_code=HTTPStatus.NO_CONTENT)

