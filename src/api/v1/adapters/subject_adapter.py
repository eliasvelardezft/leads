from domain.interfaces.adapters import IClientAdapter
from domain.models import Subject
from domain.models.value_objects import Name
from api.v1.dtos import SubjectRead, SubjectCreate


class SubjectClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(subject: SubjectCreate) -> Subject:
        return Subject(
            name=Name(name=subject.name),
            description=subject.description,
        )

    @staticmethod
    def domain_to_client(subject: Subject) -> SubjectRead:
        return SubjectRead(
            id=subject.id,
            name=subject.name.name,
            description=subject.description,
        )
