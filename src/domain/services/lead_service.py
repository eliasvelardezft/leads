from typing import Any

from domain.models.lead import Lead
from domain.interfaces import IRepository, IPaginator


class LeadService:
    def __init__(
        self,
        repository: IRepository,
        paginator: IPaginator,
    ):
        self.repository = repository
        self.paginator = paginator

    def create_lead(self, lead: Lead) -> Lead:
        return self.repository.create(lead)

    def get_leads(
        self,
        filters: dict[str, Any] = {},
    ) -> list[Lead]:
        return self.repository.filter(filters=filters)

    def get_leads_paginated(
        self,
        page: int,
        per_page: int,
        filters: dict[str, Any] = {},
    ) -> dict[str, Any]:
        paginator_instance = self.paginator(
            repository=self.repository,
            page=page,
            per_page=per_page,
            filters=filters,
        )
        return paginator_instance.get_response()

    def get_lead(self, id: str) -> Lead | None:
        return self.repository.get(id=id)
