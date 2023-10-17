from typing import Any

from domain.models.lead import Lead
from domain.interfaces.repository import IRepository


class LeadService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def create_lead(self, lead: Lead) -> Lead:
        return self.repository.create(lead)

    def get_leads(
        self,
        filters: dict[str, Any] = {},
    ) -> list[Lead]:
        return self.repository.filter(filters=filters)

    def get_lead(self, id: str) -> Lead | None:
        return self.repository.get(id=id)
