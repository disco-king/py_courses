from typing import Optional

from fastapi import Depends

from src.db import AbstractCache, AbstractSetCache
from src.db import get_access_store, get_refresh_store
from src.services import TokenStoreMixin

__all__ = (
    "StoreService",
    "get_store_service"
)


class StoreService(TokenStoreMixin):

    def store_access_token(self, jti: str):
        self.access_store.set(key=jti, value="1")

    def token_in_blacklist(self, jti: str) -> Optional[int]:
        return self.access_store.get(key=jti)

    def store_refresh_token(self, user_uuid: str, *jtis: str) -> Optional[int]:
        return self.refresh_store.sadd(user_uuid, *jtis)

    def token_in_whitelist(self, user_uuid: str, jti: str) -> Optional[set]:
        tokens = self.refresh_store.smembers(set_name=user_uuid)
        return jti in tokens

    def delete_refresh_token(self, user_uuid: str, *jtis: str) -> Optional[int]:
        return self.refresh_store.srem(user_uuid, *jtis)

    def clear_refresh_tokens(self, user_uuid: str):
        self.refresh_store.delete(user_uuid)


def get_store_service(
    access_store: AbstractCache = Depends(get_access_store),
    refresh_store: AbstractSetCache = Depends(get_refresh_store),
) -> StoreService:
    return StoreService(
        access_store=access_store,
        refresh_store=refresh_store
    )
