from datetime import datetime
from dataclasses import dataclass, field

from domain.interfaces import IStatus
from domain.models import Lead, Course
from domain.models.status import StatusChangeAction, CreatedStatus, StatusChange


@dataclass
class Enrollment:
    subject_times_taken: int
    status_changes: list[StatusChange] = field(
        default_factory=lambda: [StatusChange(
            status=CreatedStatus(),
            start_date=datetime.now()
        )]
    )
    lead: Lead | None = None
    lead_id: int | None = None
    course: Course | None = None
    course_id: int | None = None
    id: str | None = None
    created_date: str | None = None
    updated_date: str | None = None
    deleted_date: str | None = None

    def get_current_status(self) -> IStatus:
        latest_status_change = max(self.status_changes, key=lambda x: x.start_date)
        return latest_status_change.status

    def add_status_change(self, new_status: IStatus) -> None:
        new_status_change = StatusChange(status=new_status, start_date=datetime.now())
        self.status_changes.append(new_status_change)

    def change_status(self, action: StatusChangeAction) -> None:
        current_status = self.get_current_status()
        new_status_method = getattr(current_status, action, None)
        
        # TODO: test if not implented returns None.
        # if it doesnt, i need to do a try/except
        if new_status_method:
            new_status = new_status_method()
            if new_status:
                self.add_status_change(new_status)

    def progress(self) -> None:
        self.change_status(StatusChangeAction.PROGRESS)

    def complete(self) -> None:
        self.change_status(StatusChangeAction.COMPLETE)

    def fail(self) -> None:
        self.change_status(StatusChangeAction.FAIL)

    def drop(self) -> None:
        self.change_status(StatusChangeAction.DROP)
