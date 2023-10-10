from domain.services.lead_service import LeadService
from infrastructure.persistance.adapters import LeadPersistanceAdapter
from infrastructure.persistance.repositories import LeadRepository


def get_lead_service() -> LeadService:
    return LeadService(
        repository=LeadRepository(),
        persistance_adapter=LeadPersistanceAdapter(),
    )
