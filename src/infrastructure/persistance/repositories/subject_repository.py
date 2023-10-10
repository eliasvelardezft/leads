from sqlalchemy.orm import Session
from domain.interfaces import IRepository
from domain.models import Subject
from infrastructure.persistance.base import engine
from infrastructure.persistance.adapters import SubjectPersistanceAdapter
from infrastructure.persistance.models import SubjectSQL


class SubjectRepository(IRepository):
    def __init__(self, session: Session | None = None) -> None:
        if session:
            self.session = session
        else:
            self.session = Session(engine)

    def get(self, id: str) -> Subject | None:
        db_subject = self.session.query(SubjectSQL).filter(SubjectSQL.id == id).first()
        subject = None
        if db_subject:
            subject = SubjectPersistanceAdapter.persistance_to_domain(db_subject)
        return subject

    def get_all(self) -> list[Subject]:
        db_subjects = self.session.query(SubjectSQL).all()
        subjects = [SubjectPersistanceAdapter.persistance_to_domain(subject) for subject in db_subjects]
        return subjects

    def create(self, subject: Subject) -> Subject:
        db_subject = SubjectPersistanceAdapter.domain_to_persistance(subject)
        self.session.add(db_subject)
        self.session.commit()
        self.session.refresh(db_subject)
        subject = SubjectPersistanceAdapter.persistance_to_domain(db_subject)
        return subject
