from typing import Optional
import uuid

from fastapi import Depends
from sqlmodel import Session
from passlib.hash import bcrypt

from src.api.v1.schemas import UserCreate
from src.db import AbstractCache, get_cache, get_session
from src.models import User
from src.services import ServiceMixin

__all__ = ("UserService", "get_user_service")


class UserService(ServiceMixin):

    def create_user(self, user: UserCreate) -> dict:
        """Создать пользователя."""
        user_dict = user.dict()
        user_dict["uuid"] = str(uuid.uuid4())
        user_dict["password_hash"] = bcrypt.hash(user.password)
        user_dict["is_totp_enabled"] = False
        user_dict["is_superuser"] = False
        new_user = User(**user_dict)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user.dict()

    def update_user(self, data: dict) -> User:
        updated_user = User(**data)
        if "password" in data:
            updated_user.password_hash = bcrypt.hash(data["password"])
        old_user = self.session.query(User).filter(User.uuid == updated_user.uuid).first()

        self.session.delete(old_user)
        self.session.add(updated_user)
        self.session.commit()
        self.session.refresh(updated_user)
        return updated_user

    def get_user_detail(self, user_uuid: str) -> Optional[dict]:
        """Посмотреть пользователя."""
        user = self.session.query(User).filter(User.uuid == user_uuid).first()
        return user.dict() if user else None


def get_user_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> UserService:
    return UserService(cache=cache, session=session)
