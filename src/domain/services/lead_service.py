from domain.models.lead import Lead

from domain.interfaces.repository import IRepository


class LeadService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def register_lead(self, lead: Lead) -> Lead:
        return self.repository.create(lead)

    def get_lead(self, id: str) -> Lead:
        return self.repository.get(id)

    def get_all_leads(self) -> list[Lead]:
        return self.repository.get_all()
