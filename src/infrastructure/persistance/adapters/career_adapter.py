from domain.interfaces.adapters import IPersistanceAdapter
from domain.models.career import Career
from domain.models.value_objects import Name
from infrastructure.persistance.models import CareerSQL


class CareerPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(career: Career) -> CareerSQL:
        return CareerSQL(
            name=career.name.name,
            description=career.description,
        )
    
    @staticmethod
    def persistance_to_domain(career: CareerSQL) -> Career:
        return Career(
            name=Name(name=career.name),
            description=career.description,
        )
