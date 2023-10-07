from domain.interfaces.adapters import IClientAdapter, IPersistanceAdapter
from domain.models.career import Career
from domain.models.value_objects import Name
from infrastructure.db.models import CareerSQL
from api.v1.dtos.career import CareerRead


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


class CareerClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(career: CareerRead) -> Career:
        return Career(
            name=Name(name=career.name),
            description=career.description,
        )
    
    @staticmethod
    def domain_to_client(career: Career) -> CareerRead:
        return CareerRead(
            id=career.id,
            name=career.name.name,
            description=career.description,
        )
