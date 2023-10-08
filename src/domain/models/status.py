from dataclasses import dataclass
from datetime import datetime

from domain.interfaces import IStatus


@dataclass
class CreatedStatus(IStatus):
    def progress(self):
        pass

    def drop(self):
        pass


@dataclass
class InProgressStatus(IStatus):
    def complete(self):
        pass

    def fail(self):
        pass

    def drop(self):
        pass


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
