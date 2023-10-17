from typing import Any
from sqlalchemy.orm import Session
from domain.interfaces import IRepository
from domain.models import Career
from domain.exceptions import InvalidFilter
from infrastructure.persistance.base import engine
from infrastructure.persistance.adapters import CareerPersistanceAdapter
from infrastructure.persistance.models import CareerSQL


class CareerRepository(IRepository):
    def __init__(self, session: Session | None = None) -> None:
        if session:
            self.session = session
        else:
            self.session = Session(engine)

    def get(self, id: int) -> Career | None:
        db_career = self.session.get(CareerSQL, id)
        career = None
        if db_career:
            career = CareerPersistanceAdapter.persistance_to_domain(db_career)
        return career

    def create(self, career: Career) -> Career:
        db_career = CareerPersistanceAdapter.domain_to_persistance(career)
        self.session.add(db_career)
        self.session.commit()
        self.session.refresh(db_career)
        career = CareerPersistanceAdapter.persistance_to_domain(db_career)
        return career

    def filter(self, filters: dict[str, Any] = {}) -> list[Career]:
        query = self.session.query(CareerSQL)

        for key, value in filters.items():
            try:
                query = query.filter(getattr(CareerSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_careers = query.all() 
        careers = [CareerPersistanceAdapter.persistance_to_domain(career) for career in db_careers]
        return careers

