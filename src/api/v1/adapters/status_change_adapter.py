from domain.interfaces.adapters import IClientAdapter
from domain.models.status import StatusChange
from api.v1.dtos import StatusChangeRead
from api.v1.adapters.status_adapter import StatusClientAdapter


class StatusChangeClientAdapter(IClientAdapter):
    @staticmethod
    def domain_to_client(status_change: StatusChange) -> StatusChangeRead:
        return StatusChangeRead(
            id=status_change.id,
            start_date=status_change.start_date,
            end_date=status_change.end_date,
            status=status_change.status.status,
        )
    
    @staticmethod
    def client_to_domain(status_change: StatusChangeRead) -> StatusChange:
        domain_status = StatusClientAdapter.client_to_domain(
            status=status_change.status
        )
        return StatusChange(
            id=status_change.id,
            start_date=status_change.start_date,
            end_date=status_change.end_date,
            status=domain_status,
        )
