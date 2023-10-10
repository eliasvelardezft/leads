from api.v1.dtos.lead import LeadCreate, LeadRead
from domain.interfaces import IClientAdapter
from domain.models.lead import Lead
from domain.models.value_objects import Name, Email


class LeadClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(lead: LeadCreate) -> Lead:
        return Lead(
            first_name=Name(name=lead.first_name),
            last_name=Name(name=lead.last_name),
            email=Email(email=lead.email),
        )

    @staticmethod
    def domain_to_client(lead: Lead) -> LeadRead:
        return LeadRead(
            id=lead.id,
            first_name=lead.first_name.name,
            last_name=lead.last_name.name,
            email=lead.email.email,
        )
