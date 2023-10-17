from api.v1.dtos.lead import LeadCreate, LeadRead
from domain.interfaces import IClientAdapter
from domain.models import Lead
from domain.models.value_objects import Name, Email, PhoneNumber, Year
from api.v1.adapters.address_adapter import AddressClientAdapter
from api.v1.adapters.career_adapter import CareerClientAdapter


class LeadClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(lead: LeadCreate) -> Lead:
        domain_address = AddressClientAdapter.client_to_domain(lead.address)
        return Lead(
            first_name=Name(name=lead.first_name),
            last_name=Name(name=lead.last_name),
            email=Email(email=lead.email),
            phone_number=PhoneNumber(number=lead.phone_number),
            address=domain_address,
            career_id=lead.career_id,
            year_of_inscription=Year(year=lead.year_of_inscription),
        )

    @staticmethod
    def domain_to_client(lead: Lead) -> LeadRead:
        client_address = AddressClientAdapter.domain_to_client(lead.address)
        client_career = CareerClientAdapter.domain_to_client(lead.career)
        return LeadRead(
            id=lead.id,
            first_name=lead.first_name.name,
            last_name=lead.last_name.name,
            email=lead.email.email,
            phone_number=lead.phone_number.number,
            year_of_inscription=lead.year_of_inscription.year,
            career_id=lead.career.id,
            career=client_career,
            address=client_address,
        )
