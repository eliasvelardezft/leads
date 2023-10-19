from abc import ABC
from typing import Any


class IRepository(ABC):
    def get(id: str) -> Any:
        raise NotImplementedError

    def filter(filter: dict[str, Any] = {}) -> list[Any]:
        raise NotImplementedError

    def paginated_filter(
        offset: int,
        limit: int,
        filters: dict[str, Any] = {},
    ) -> list[Any]:
        raise NotImplementedError

    def create(object: Any) -> Any:
        raise NotImplementedError

    def update(id: str, object_update: Any) -> Any:
        raise NotImplementedError

    def delete(id: str):
        raise NotImplementedError
