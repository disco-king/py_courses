from datetime import datetime
from typing import Optional, List

from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint

__all__ = ("User",)


class User(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("username"),
        UniqueConstraint("email")
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False)
    password_hash: str = Field(nullable=False)
    is_superuser: bool = Field(default=0)
    uuid: str = Field(nullable=False)
    is_totp_enabled: bool = Field(default=0)
    email: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
