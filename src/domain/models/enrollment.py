from datetime import datetime
from dataclasses import dataclass

from interfaces.status import IStatus
from .lead import Lead
from .subject import Subject
from .status import StatusChange
from .course import Course


@dataclass
class Enrollment:
    lead: Lead
    course: Course
    subjet_times_taken: int
    created_date: datetime

    status_changes: list[StatusChange]


    def get_current_status(self) -> IStatus:
        return self.status_changes.sort(
            key=lambda status: status.start_date,
            reverse=True
        )[0].status
