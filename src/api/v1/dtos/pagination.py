from dataclasses import dataclass
from fastapi import Query


@dataclass
class PaginatedResponse:
    count: int
    next_page: int | None
    previous_page: int | None
    results: list


class PaginationParams:
    def __init__(
        self,
        page: int = Query(1, ge=1),
        per_page: int = Query(100, ge=0),
    ):
        self.page = page
        self.per_page = per_page
