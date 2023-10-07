from api.v1.dtos.lead import LeadCreate, LeadRead
from domain.interfaces import IPersistanceAdapter, IClientAdapter
from domain.models.lead import Lead
from domain.models.value_objects import Name, Email, PhoneNumber, Year
from infrastructure.db.models import LeadSQL
from infrastructure.repositories import CareerRepository
from .address_adapters import AddressClientAdapter
from .career_adapters import CareerClientAdapter, CareerPersistanceAdapter


class LeadPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(lead: Lead) -> LeadSQL:
        return LeadSQL(
            id=lead.id,
            first_name=lead.first_name.name,
            last_name=lead.last_name.name,
            email=lead.email.email,
        )

    @staticmethod
    def persistance_to_domain(lead: LeadSQL) -> Lead:
        return Lead(
            id=lead.id,
            first_name=Name(name=lead.first_name),
            last_name=Name(name=lead.last_name),
            email=Email(email=lead.email),
        )


class LeadClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(lead: LeadCreate) -> Lead:
        db_career = CareerRepository.get(lead.career_id)
        domain_career = CareerPersistanceAdapter.persistance_to_domain(db_career)
        domain_address = AddressClientAdapter.client_to_domain(lead.address)
        return Lead(
            first_name=Name(name=lead.first_name),
            last_name=Name(name=lead.last_name),
            email=Email(email=lead.email),
            phone_number=PhoneNumber(number=lead.phone_number),
            address=domain_address,
            career=domain_career,
            year_of_inscription=Year(year=lead.year_of_inscription),

        )

    @staticmethod
    def domain_to_client(lead: Lead) -> LeadRead:
        client_address = AddressClientAdapter.domain_to_client(lead.address)
        client_carreer = CareerClientAdapter.domain_to_client(lead.career)
        return LeadRead(
            id=lead.id,
            first_name=lead.first_name.name,
            last_name=lead.last_name.name,
            email=lead.email.email,
            phone_number=lead.phone_number.number,
            address=client_address,
            career=client_carreer,
            year_of_inscription=lead.year_of_inscription.year,
        )
