from typing import Any
from datetime import datetime

from domain.models.enrollment import Enrollment
from domain.models.status import IStatus, StatusChange, CreatedStatus
from domain.interfaces.repository import IRepository


class EnrollmentService:
    def __init__(
        self,
        repository: IRepository,
        status_change_repository: IRepository,
    ):
        self.repository = repository
        self.status_change_repository = status_change_repository

    def create_enrollment(self, enrollment: Enrollment) -> Enrollment:
        return self.repository.create(enrollment)

    def create_enrollments(self, enrollments: list[Enrollment]) -> list[Enrollment]:
        return self.repository.bulk_create(enrollments)

    def get_enrollments(
        self,
        filters: dict[str, Any] = {},
    ) -> list[Enrollment]:
        return self.repository.filter(filters=filters)

    def get_enrollment(self, id: str) -> Enrollment | None:
        return self.repository.get(id=id)
