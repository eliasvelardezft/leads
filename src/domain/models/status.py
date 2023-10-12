from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from domain.interfaces import IStatus


class StatusChangeAction(str, Enum):
    COMPLETE = "complete"
    PROGRESS = "progress"
    FAIL = "fail"
    DROP = "drop"


class EnrollmentStatus(str, Enum):
    CREATED = "created"
    COMPLETED = "completed"
    PROGRESS = "progress"
    FAILED = "failed"
    DROPPED = "dropped"


@dataclass
class CreatedStatus(IStatus):
    status: EnrollmentStatus = EnrollmentStatus.CREATED

    def progress(self):
        return ProgressStatus()

    def drop(self):
        return DroppedStatus()


@dataclass
class ProgressStatus(IStatus):
    status: EnrollmentStatus = EnrollmentStatus.PROGRESS

    def complete(self):
        return CompletedStatus()

    def fail(self):
        return FailedStatus()

    def drop(self):
        return DroppedStatus()


@dataclass
class CompletedStatus(IStatus):
    status: EnrollmentStatus = EnrollmentStatus.COMPLETED


@dataclass
class FailedStatus(IStatus):
    status: EnrollmentStatus = EnrollmentStatus.FAILED


@dataclass
class DroppedStatus(IStatus):
    status: EnrollmentStatus = EnrollmentStatus.DROPPED


@dataclass
class StatusChange:
    status: IStatus
    
    start_date: datetime
    end_date: datetime | None = None

    id: str | None = None
    created_date: str | None = None
    updated_date: str | None = None
    deleted_date: str | None = None
