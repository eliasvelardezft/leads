from typing import Any

from sqlalchemy.orm import Session

from domain.interfaces import IRepository
from domain.models import Enrollment
from domain.exceptions import InvalidFilter
from infrastructure.persistance.base import engine
from infrastructure.persistance.adapters import EnrollmentPersistanceAdapter
from infrastructure.persistance.models import EnrollmentSQL


class EnrollmentRepository(IRepository):
    def __init__(self, session: Session | None = None) -> None:
        if session:
            self.session = session
        else:
            self.session = Session(engine)

    def get(self, id: str) -> Enrollment | None:
        db_enrollment = self.session.query(EnrollmentSQL).filter(EnrollmentSQL.id == id).first()
        enrollment = None
        if db_enrollment:
            enrollment = EnrollmentPersistanceAdapter.persistance_to_domain(db_enrollment)
        return enrollment

    def filter(self, filters: dict[str, Any]) -> list[Enrollment]:
        query = self.session.query(EnrollmentSQL)
        for key, value in filters.items():
            try:
                query = query.filter(getattr(EnrollmentSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_enrollments = query.all()
        enrollments = [EnrollmentPersistanceAdapter.persistance_to_domain(enrollment) for enrollment in db_enrollments]
        return enrollments

    def filter_by_lead(self, filters: dict[str, Any]) -> list[Enrollment]:
        query = self.session.query(EnrollmentSQL).join(EnrollmentSQL.lead)
        for key, value in filters.items():
            try:
                query = query.filter(
                    getattr(EnrollmentSQL.lead.property.mapper.class_, key) == value
                )
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_enrollments = query.all()
        enrollments = [EnrollmentPersistanceAdapter.persistance_to_domain(enrollment) for enrollment in db_enrollments]
        return enrollments

    def create(self, enrollment: Enrollment) -> Enrollment:
        db_enrollment = EnrollmentPersistanceAdapter.domain_to_persistance(enrollment)
        self.session.add(db_enrollment)
        self.session.commit()
        self.session.refresh(db_enrollment)
        enrollment = EnrollmentPersistanceAdapter.persistance_to_domain(db_enrollment)
        return enrollment

    def bulk_create(self, enrollments: list[Enrollment]) -> list[Enrollment]:
        db_enrollments = [
            EnrollmentPersistanceAdapter.domain_to_persistance(enrollment)
            for enrollment in enrollments
        ]
        self.session.bulk_save_objects(db_enrollments)
        self.session.commit()

        db_enrollments = self.session.query(EnrollmentSQL).filter(
            EnrollmentSQL.id.in_([enrollment.id for enrollment in db_enrollments])
        ).all()

        enrollments = [
            EnrollmentPersistanceAdapter.persistance_to_domain(enrollment)
            for enrollment in db_enrollments
        ]
        return enrollments
