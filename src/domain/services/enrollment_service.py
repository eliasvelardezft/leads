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

    def register_enrollment(self, enrollment: Enrollment) -> Enrollment:
        # status_change = StatusChange(
        #     start_date=datetime.now(),
        #     status=CreatedStatus(),
        # )
        # enrollment.
        return self.repository.create(enrollment)

    def filter_enrollments(
        self,
        filters: dict[str, Any],
    ) -> list[Enrollment]:
        if filters:
            return self.repository.filter(filters=filters)
        else:
            return self.get_all_enrollments()

    def filter_by_lead(
        self,
        filters: dict[str, Any],
    ) -> list[Enrollment]:
        if filters:
            return self.repository.filter_by_lead(filters=filters)
        else:
            return self.get_all_enrollments()

    def get_enrollment(self, id: str) -> Enrollment | None:
        return self.repository.get(id=id)

    def get_all_enrollments(self) -> list[Enrollment]:
        return self.repository.get_all()
