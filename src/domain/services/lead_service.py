from typing import Any

from domain.models.lead import Lead
from domain.interfaces.repository import IRepository


class LeadService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def register_lead(self, lead: Lead) -> Lead:
        return self.repository.create(lead)

    def filter_leads(
        self,
        filters: dict[str, Any],
    ) -> list[Lead]:
        if filters:
            return self.repository.filter(filters=filters)
        else:
            return self.get_all_leads()

    def get_lead(self, id: str) -> Lead | None:
        return self.repository.get(id=id)

    def get_all_leads(self) -> list[Lead]:
        return self.repository.get_all()
