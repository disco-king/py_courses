from sqlmodel import Session

from src.db import AbstractCache


class ServiceMixin:
    def __init__(self, cache: AbstractCache, session: Session):
        self.cache: AbstractCache = cache
        self.session: Session = session


class TokenStoreMixin:
    def __init__(
        self,
        access_store: AbstractCache,
        refresh_store: AbstractCache
    ):
        self.access_store: AbstractCache = access_store
        self.refresh_store: AbstractCache = refresh_store
