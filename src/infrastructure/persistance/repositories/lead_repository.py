from typing import Any

from sqlalchemy.orm import Session

from domain.interfaces import IRepository
from domain.models import Lead
from infrastructure.persistance.exceptions import InvalidFilter
from infrastructure.persistance.base import engine
from infrastructure.persistance.adapters import LeadPersistanceAdapter
from infrastructure.persistance.models import LeadSQL


class LeadRepository(IRepository):
    def __init__(self, session: Session | None = None) -> None:
        if session:
            self.session = session
        else:
            self.session = Session(engine)

    def get(self, id: str) -> Lead | None:
        db_lead = self.session.query(LeadSQL).filter(LeadSQL.id == id).first()
        lead = None
        if db_lead:
            lead = LeadPersistanceAdapter.persistance_to_domain(db_lead)
        return lead

    def filter(self, filters: dict[str, Any]) -> list[Lead]:
        query = self.session.query(LeadSQL)
        for key, value in filters.items():
            try:
                query = query.filter(getattr(LeadSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_leads = query.all()
        leads = [LeadPersistanceAdapter.persistance_to_domain(lead) for lead in db_leads]
        return leads

    def create(self, lead: Lead) -> Lead:
        db_lead = LeadPersistanceAdapter.domain_to_persistance(lead)
        self.session.add(db_lead)
        self.session.commit()
        self.session.refresh(db_lead)
        lead = LeadPersistanceAdapter.persistance_to_domain(db_lead)
        return lead
