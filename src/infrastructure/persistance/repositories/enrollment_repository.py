from typing import Any

from psycopg2 import errors
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from domain.interfaces import IRepository
from domain.models import Enrollment
from domain.exceptions import InvalidFilter, LeadAlreadyEnrolledToCourse, LeadDoesNotExist
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
        db_enrollment = self.session.get(EnrollmentSQL, id)
        enrollment = None
        if db_enrollment:
            enrollment = EnrollmentPersistanceAdapter.persistance_to_domain(db_enrollment)
        return enrollment

    def filter(self, filters: dict[str, Any] = {}) -> list[Enrollment]:
        query = self.session.query(EnrollmentSQL).join(EnrollmentSQL.lead)
        for key, value in filters.items():
            try:
                if key == "lead":
                    for k, v in value.items():
                        query = query.filter(
                            getattr(EnrollmentSQL.lead.property.mapper.class_, k) == v
                        )
                else:
                    query = query.filter(getattr(EnrollmentSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_enrollments = query.all()
        enrollments = [EnrollmentPersistanceAdapter.persistance_to_domain(enrollment) for enrollment in db_enrollments]
        return enrollments

    def create(self, enrollment: Enrollment) -> Enrollment:
        db_enrollment = EnrollmentPersistanceAdapter.domain_to_persistance(enrollment)
        self.session.add(db_enrollment)
        try:
            self.session.commit()
        except IntegrityError as sa_error:
            try:
                raise sa_error.orig
            except errors.ForeignKeyViolation:
                raise LeadDoesNotExist
            except errors.UniqueViolation:
                raise LeadAlreadyEnrolledToCourse
        self.session.refresh(db_enrollment)
        enrollment = EnrollmentPersistanceAdapter.persistance_to_domain(db_enrollment)
        return enrollment

    def bulk_create(self, enrollments: list[Enrollment]) -> list[Enrollment]:
        db_enrollments = [
            EnrollmentPersistanceAdapter.domain_to_persistance(enrollment)
            for enrollment in enrollments
        ]
        self.session.add_all(db_enrollments)

        try:
            self.session.commit()
        except IntegrityError as sa_error:
            try:
                raise sa_error.orig
            except errors.ForeignKeyViolation:
                raise LeadDoesNotExist
            except errors.UniqueViolation:
                raise LeadAlreadyEnrolledToCourse

        enrollments = [
            EnrollmentPersistanceAdapter.persistance_to_domain(enrollment)
            for enrollment in db_enrollments
        ]
        return enrollments
