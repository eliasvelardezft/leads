from domain.interfaces.adapters import IPersistanceAdapter
from domain.models.status import StatusChange
from infrastructure.persistance.models import StatusChangeSQL
from infrastructure.persistance.adapters.status_adapter import StatusPersistanceAdapter


class StatusChangePersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(status_change: StatusChange) -> StatusChangeSQL:
        return StatusChangeSQL(
            start_date=status_change.start_date,
            end_date=status_change.end_date,
            status=status_change.status.status,
        )
    
    @staticmethod
    def persistance_to_domain(status_change: StatusChangeSQL) -> StatusChange:
        domain_status = StatusPersistanceAdapter.persistance_to_domain(
            status=status_change.status
        )
        return StatusChange(
            id=status_change.id,
            start_date=status_change.start_date,
            end_date=status_change.end_date,
            status=domain_status,
        )
