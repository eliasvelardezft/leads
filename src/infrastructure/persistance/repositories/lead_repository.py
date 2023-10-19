from typing import Any

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from domain.interfaces import IRepository
from domain.models import Lead
from domain.exceptions import InvalidFilter, LeadAlreadyExists
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
        db_lead = self.session.get(LeadSQL, id)
        lead = None
        if db_lead:
            lead = LeadPersistanceAdapter.persistance_to_domain(db_lead)
        return lead

    def filter(self, filters: dict[str, Any] = {}) -> list[Lead]:
        query = self.session.query(LeadSQL)
        for key, value in filters.items():
            try:
                query = query.filter(getattr(LeadSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_leads = query.all()
        leads = [LeadPersistanceAdapter.persistance_to_domain(lead) for lead in db_leads]
        return leads
    
    def pagination_filter(
        self,
        offset: int | None = None,
        limit: int | None = None,
        filters: dict[str, Any] = {},
    ) -> dict[str, list[Lead] | int]:
        query = self.session.query(LeadSQL)
        for key, value in filters.items():
            try:
                query = query.filter(getattr(LeadSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")

        count = query.count()
        if not offset and not limit:
            return {
                "count": count,
                "results": [],
            }
        db_leads = query.offset(offset).limit(limit).all()
        leads = [LeadPersistanceAdapter.persistance_to_domain(lead) for lead in db_leads]
        return {
            "count": count,
            "results": leads,
        }

    def create(self, lead: Lead) -> Lead:
        db_lead = LeadPersistanceAdapter.domain_to_persistance(lead)
        self.session.add(db_lead)
        try:
            self.session.commit()
        except IntegrityError:
            raise LeadAlreadyExists
        self.session.refresh(db_lead)
        lead = LeadPersistanceAdapter.persistance_to_domain(db_lead)
        return lead
