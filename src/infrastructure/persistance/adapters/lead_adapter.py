from domain.interfaces import IPersistanceAdapter
from domain.models.lead import Lead
from domain.models.value_objects import Name, Email, PhoneNumber, Year
from infrastructure.persistance.models import LeadSQL
from infrastructure.persistance.adapters.address_adapter import AddressPersistanceAdapter
from infrastructure.persistance.adapters.career_adapter import CareerPersistanceAdapter

class LeadPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(lead: Lead) -> LeadSQL:
        persistance_address = AddressPersistanceAdapter.domain_to_persistance(lead.address)
        return LeadSQL(
            id=lead.id,
            first_name=lead.first_name.name,
            last_name=lead.last_name.name,
            email=lead.email.email,
            career_id=lead.career_id,
            phone_number=lead.phone_number.number,
            address=persistance_address,
            year_of_inscription=lead.year_of_inscription.year,
        )

    @staticmethod
    def persistance_to_domain(lead: LeadSQL) -> Lead:
        domain_address = AddressPersistanceAdapter.persistance_to_domain(lead.address)
        domain_career = CareerPersistanceAdapter.persistance_to_domain(lead.career)
        return Lead(
            id=lead.id,
            first_name=Name(name=lead.first_name),
            last_name=Name(name=lead.last_name),
            email=Email(email=lead.email),
            phone_number=PhoneNumber(number=lead.phone_number),
            address=domain_address,
            year_of_inscription=Year(year=lead.year_of_inscription),
            career_id=lead.career_id,
            career=domain_career,
        )
