from typing import NoReturn, Optional, Union

from src.core import config
from src.db import AbstractCache, AbstractSetCache

__all__ = (
    "CacheRedis",
    "StoreRedis",
    "SetStoreRedis"
)


class CacheRedis(AbstractCache):
    def get(self, key: str) -> Optional[dict]:
        return self.cache.get(name=key)

    def set(
        self,
        key: str,
        value: Union[bytes, str],
        expire: int = config.CACHE_EXPIRE_IN_SECONDS,
    ):
        self.cache.set(name=key, value=value, ex=expire)

    def close(self) -> NoReturn:
        self.cache.close()


class StoreRedis(AbstractCache):
    def get(self, key: str) -> Optional[int]:
        return int(self.cache.exists(key))

    def set(
        self,
        key: str,
        value: Union[bytes, str],
        expire: int = int(config.JWT_EXPIRATION_TIME) * 60,
    ):
        self.cache.set(name=key, value=value, ex=expire)

    def close(self) -> NoReturn:
        self.cache.close()


class SetStoreRedis(AbstractSetCache):
    def smembers(self, set_name: str) -> Optional[set]:
        return self.store.smembers(name=set_name)

    def sadd(
        self,
        set_name: str,
        *values: Union[bytes, str]
    ):
        return self.store.sadd(set_name, *values)

    def srem(
        self,
        set_name: str,
        *values: Union[bytes, str]
    ):
        return self.store.srem(set_name, *values)

    def delete(self, set_name: str):
        self.store.delete(set_name)

    def close(self) -> NoReturn:
        self.store.close()
