from domain.interfaces.adapters import IClientAdapter
from domain.models import (
    IStatus,
    EnrollmentStatus,
    CreatedStatus,
    ProgressStatus,
    CompletedStatus,
    FailedStatus,
    DroppedStatus,
)


class StatusClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(status: EnrollmentStatus) -> IStatus:
        return {
            EnrollmentStatus.CREATED: CreatedStatus(),
            EnrollmentStatus.PROGRESS: ProgressStatus(),
            EnrollmentStatus.COMPLETED: CompletedStatus(),
            EnrollmentStatus.FAILED: FailedStatus(),
            EnrollmentStatus.DROPPED: DroppedStatus(),
        }.get(status, CreatedStatus())
    
    @staticmethod
    def domain_to_client(status: IStatus) -> EnrollmentStatus:
        return status.status
