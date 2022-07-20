from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

__all__ = (
    "UserModel",
    "UserCreate",
    "Token"
)


class UserBase(BaseModel):
    username: str
    email:str


class UserCreate(UserBase):
    password: str


class UserModel(UserBase):
    id: int 
    is_superuser: bool
    is_totp_enabled: bool
    is_active: bool = True
    uuid: str
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"