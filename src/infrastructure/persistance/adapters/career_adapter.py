from domain.interfaces.adapters import IPersistanceAdapter
from domain.models.career import Career
from domain.models.value_objects import Name
from infrastructure.persistance.models import CareerSQL
from .subject_adapter import SubjectPersistanceAdapter


class CareerPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(career: Career) -> CareerSQL:
        return CareerSQL(
            name=career.name.name,
            description=career.description,
            subject_ids=career.subject_ids,
        )

    @staticmethod
    def persistance_to_domain(career: CareerSQL) -> Career:
        domain_subjects = [
            SubjectPersistanceAdapter.persistance_to_domain(subject)
            for subject in career.subjects
        ]
        return Career(
            id=career.id,
            name=Name(name=career.name),
            description=career.description,
            subject_ids=career.subject_ids,
            subjects=domain_subjects,
        )
