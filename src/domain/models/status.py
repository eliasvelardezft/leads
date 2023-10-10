from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from domain.interfaces import IStatus


class StatusChangeAction(str, Enum):
    COMPLETE = "complete"
    PROGRESS = "progress"
    FAIL = "fail"
    DROP = "drop"


@dataclass
class CreatedStatus(IStatus):
    def progress(self):
        return ProgressStatus()

    def drop(self):
        return DroppedStatus()


@dataclass
class ProgressStatus(IStatus):
    def complete(self):
        return CompletedStatus()

    def fail(self):
        return FailedStatus()

    def drop(self):
        return DroppedStatus()


@dataclass
class CompletedStatus(IStatus):
    pass


@dataclass
class FailedStatus(IStatus):
    pass


@dataclass
class DroppedStatus(IStatus):
    pass


@dataclass
class StatusChange:
    status: IStatus
    
    start_date: datetime
    end_date: datetime

    id: str | None = None
    created_date: str | None = None
    updated_date: str | None = None
    deleted_date: str | None = None
