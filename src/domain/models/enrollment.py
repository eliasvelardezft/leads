from datetime import datetime
from dataclasses import dataclass

from .lead import Lead
from .subject import Subject
from .status import StatusChange


@dataclass
class Enrollment:
    lead: Lead
    subject: Subject
    subjet_times_taken: int

    status_changes: list[StatusChange]

    created_date: datetime
    starting_date: datetime

    def get_current_status(self):
        return self.status_changes.sort(
            key=lambda status: status.start_date,
            reverse=True
        )[0].status
