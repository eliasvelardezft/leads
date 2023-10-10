from domain.interfaces.adapters import IClientAdapter
from domain.models.career import Career
from domain.models.value_objects import Name
from api.v1.dtos.career import CareerCreate, CareerRead


class CareerClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(career: CareerCreate) -> Career:
        return Career(
            name=Name(name=career.name),
            description=career.description,
            subject_ids=career.subject_ids,
        )
    
    @staticmethod
    def domain_to_client(career: Career) -> CareerRead:
        return CareerRead(
            id=career.id,
            name=career.name.name,
            description=career.description,
            subject_ids=career.subject_ids,
        )
