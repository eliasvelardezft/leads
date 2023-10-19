from abc import ABC
from typing import Any

from domain.interfaces import IRepository


class IPaginator(ABC):
    def __init__(
        self,
        repository: IRepository,
        page: int,
        per_page: int,
        filters: dict[str, Any] = {}
    ):
        raise NotImplementedError

    def get_response(self) -> dict[str, Any]:
        raise NotImplementedError
