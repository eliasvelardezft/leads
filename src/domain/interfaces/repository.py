from abc import ABC
from typing import Any


class IRepository(ABC):
    def get(id: str) -> Any:
        raise NotImplementedError

    def get_all() -> list[Any]:
        raise NotImplementedError

    def create(object: Any) -> Any:
        raise NotImplementedError

    def update(id: str, object_update: Any) -> Any:
        raise NotImplementedError

    def delete(id: str):
        raise NotImplementedError
