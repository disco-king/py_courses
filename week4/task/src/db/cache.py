from abc import ABC, abstractmethod
from typing import Optional, Union

from src.core import config


__all__ = (
    "AbstractCache",
    "AbstractSetCache",
    "get_cache",
    "get_access_store",
    "get_refresh_store",
)


class AbstractCache(ABC):
    def __init__(self, cache_instance):
        self.cache = cache_instance

    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(
        self,
        key: str,
        value: Union[bytes, str],
        expire: int = config.CACHE_EXPIRE_IN_SECONDS,
    ):
        pass

    @abstractmethod
    def close(self):
        pass

class AbstractSetCache(ABC):
    def __init__(self, store_instance):
        self.store = store_instance

    @abstractmethod
    def smembers(self, set_name: str) -> Optional[set]:
        pass

    @abstractmethod
    def sadd(
        self,
        set_name: str,
        *values: Union[bytes, str]
    ):
        pass

    @abstractmethod
    def srem(
        self,
        set_name: str,
        *values: Union[bytes, str]
    ):
        pass

    @abstractmethod
    def close(self):
        pass


cache: Optional[AbstractCache] = None
access_store: Optional[AbstractCache] = None
refresh_store: Optional[AbstractSetCache] = None


# Функции понадобятся при внедрении зависимостей

def get_cache() -> AbstractCache:
    return cache

def get_access_store() -> AbstractCache:
    return access_store

def get_refresh_store() -> AbstractSetCache:
    return refresh_store
