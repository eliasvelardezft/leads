from domain.models.lead import Lead

from infrastructure.repositories import LeadRepository
from infrastructure.adapters.lead_adapters import LeadPersistanceAdapter


class LeadService:
    def __init__(
        self,
        repository: LeadRepository,
        persistance_adapter: LeadPersistanceAdapter
    ):
        self.repository = repository
        self.persistance_adapter = persistance_adapter

    def register_lead(self, lead: Lead) -> Lead:
        lead_sql = self.persistance_adapter.domain_to_persistance(lead)
        lead_sql = self.repository.create(lead_sql)
        lead = self.persistance_adapter.persistance_to_domain(lead_sql)
        return lead

    def get_lead(self, id: str) -> Lead:
        lead_sql = self.repository.get(id)
        lead = self.persistance_adapter.persistance_to_domain(lead_sql)
        return lead

    def get_all_leads(self) -> list[Lead]:
        leads_sql = self.repository.get_all()
        leads = [
            self.persistance_adapter.persistance_to_domain(lead_sql)
            for lead_sql in leads_sql
        ]
        return leads
