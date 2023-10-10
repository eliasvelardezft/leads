from sqlalchemy.orm import Session
from domain.interfaces import IRepository
from domain.models import Career
from infrastructure.persistance.base import engine
from infrastructure.persistance.adapters import CareerPersistanceAdapter
from infrastructure.persistance.models import CareerSQL


class CareerRepository(IRepository):
    def __init__(self, session: Session | None = None) -> None:
        if session:
            self.session = session
        else:
            self.session = Session(engine)

    def get(self, id: str) -> Career | None:
        db_career = self.session.query(CareerSQL).filter(CareerSQL.id == id).first()
        career = None
        if db_career:
            career = CareerPersistanceAdapter.persistance_to_domain(db_career)
        return career

    def get_all(self) -> list[Career]:
        db_careers = self.session.query(CareerSQL).all()
        careers = [CareerPersistanceAdapter.persistance_to_domain(career) for career in db_careers]
        return careers

    def create(self, career: Career) -> Career:
        db_career = CareerPersistanceAdapter.domain_to_persistance(career)
        self.session.add(db_career)
        self.session.commit()
        self.session.refresh(db_career)
        career = CareerPersistanceAdapter.persistance_to_domain(db_career)
        return career
