from domain.services.lead_service import LeadService
from infrastructure.adapters.lead_adapters import LeadPersistanceAdapter
from infrastructure.repositories import LeadRepository


def get_lead_service() -> LeadService:
    return LeadService(
        repository=LeadRepository(),
        persistance_adapter=LeadPersistanceAdapter(),
    )
