from domain.interfaces.adapters import IPersistanceAdapter
from domain.models import (
    IStatus,
    EnrollmentStatus,
    CreatedStatus,
    ProgressStatus,
    CompletedStatus,
    FailedStatus,
    DroppedStatus,
)


class StatusPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def persistance_to_domain(status: EnrollmentStatus) -> IStatus:
        return {
            EnrollmentStatus.CREATED: CreatedStatus(),
            EnrollmentStatus.PROGRESS: ProgressStatus(),
            EnrollmentStatus.COMPLETED: CompletedStatus(),
            EnrollmentStatus.FAILED: FailedStatus(),
            EnrollmentStatus.DROPPED: DroppedStatus(),
        }.get(status, CreatedStatus())
    
    @staticmethod
    def domain_to_persistance(status: IStatus) -> EnrollmentStatus:
        return status.status
