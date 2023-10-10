from domain.interfaces.adapters import IPersistanceAdapter
from domain.models.subject import Subject
from domain.models.value_objects import Name
from infrastructure.persistance.models import SubjectSQL


class SubjectPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(subject: Subject) -> SubjectSQL:
        return SubjectSQL(
            name=subject.name.name,
            description=subject.description,
        )
    
    @staticmethod
    def persistance_to_domain(subject: SubjectSQL) -> Subject:
        return Subject(
            id=subject.id,
            name=Name(name=subject.name),
            description=subject.description,
        )
