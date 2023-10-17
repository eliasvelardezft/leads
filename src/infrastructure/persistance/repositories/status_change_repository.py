from typing import Any

from sqlalchemy.orm import Session

from domain.interfaces import IRepository
from domain.models import StatusChange
from domain.exceptions import InvalidFilter
from infrastructure.persistance.base import engine
from infrastructure.persistance.adapters import StatusChangePersistanceAdapter
from infrastructure.persistance.models import StatusChangeSQL


class StatusChangeRepository(IRepository):
    def __init__(self, session: Session | None = None) -> None:
        if session:
            self.session = session
        else:
            self.session = Session(engine)

    def get(self, id: str) -> StatusChange | None:
        db_status_change = self.session.query(StatusChangeSQL).filter(StatusChangeSQL.id == id).first()
        status_change = None
        if db_status_change:
            status_change = StatusChangePersistanceAdapter.persistance_to_domain(db_status_change)
        return status_change

    def filter(self, filters: dict[str, Any] = {}) -> list[StatusChange]:
        query = self.session.query(StatusChangeSQL)
        for key, value in filters.items():
            try:
                query = query.filter(getattr(StatusChangeSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_status_changes = query.all()
        status_changes = [StatusChangePersistanceAdapter.persistance_to_domain(status_change) for status_change in db_status_changes]
        return status_changes

    def create(self, status_change: StatusChange) -> StatusChange:
        db_status_change = StatusChangePersistanceAdapter.domain_to_persistance(status_change)
        self.session.add(db_status_change)
        self.session.commit()
        self.session.refresh(db_status_change)
        status_change = StatusChangePersistanceAdapter.persistance_to_domain(db_status_change)
        return status_change
