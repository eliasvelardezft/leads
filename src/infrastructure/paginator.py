from typing import Any

from domain.interfaces import IRepository


class Paginator:
    def __init__(
        self,
        repository: IRepository,
        page: int,
        per_page: int,
        filters: dict[str, Any] = {}
    ):
        self.page = page
        self.per_page = per_page
        self.repository = repository
        self.limit = per_page
        self.offset = (page - 1) * per_page
        self.filters = filters

        self.number_of_pages = 0
        self.next_page = ''
        self.previous_page = ''

    def _get_next_page(self) -> int | None:
        if self.page >= self.number_of_pages:
            return
        return self.page + 1

    def _get_previous_page(self) -> int | None:
        if (
            self.page == 1 or
            self.page > self.number_of_pages + 1
        ):
            return
        return self.page - 1

    def _get_results(self) -> list[dict]:
        offset = self.offset
        limit = self.limit
        results = self.repository.pagination_filter(
            limit=limit,
            offset=offset,
            filters=self.filters,
        ).get("results")
        return results

    def _get_number_of_pages(self, count: int) -> int:
        rest = count % self.per_page
        pages = count // self.per_page
        return pages if not rest else pages + 1

    def _get_total_count(self) -> int:
        count = self.repository.pagination_filter(filters=self.filters).get("count")
        self.number_of_pages = self._get_number_of_pages(count)
        return count

    def get_response(self) -> dict:
        return {
            'count': self._get_total_count(),
            'next_page': self._get_next_page(),
            'previous_page': self._get_previous_page(),
            'results': self._get_results(),
        }
