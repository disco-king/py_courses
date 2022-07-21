from datetime import datetime
from typing import Optional

from pydantic import BaseModel

__all__ = (
    "UserModel",
    "UserCreate",
    "UserUpdate",
    "UserLogin",
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


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"