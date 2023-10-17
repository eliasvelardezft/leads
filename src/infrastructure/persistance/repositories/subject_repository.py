from typing import Any

from sqlalchemy.orm import Session

from domain.interfaces import IRepository
from domain.models import Subject
from domain.exceptions import InvalidFilter
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
        db_subject = self.session.get(SubjectSQL, id)
        subject = None
        if db_subject:
            subject = SubjectPersistanceAdapter.persistance_to_domain(db_subject)
        return subject
    
    def filter(self, filters: dict[str, Any] = {}) -> list[Subject]:
        query = self.session.query(SubjectSQL)
        for key, value in filters.items():
            try:
                if key == 'career_id':
                    query = query.join(
                        SubjectSQL.careers
                    ).filter(SubjectSQL.careers.any(id=value))
                else:
                    query = query.filter(getattr(SubjectSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_Subjects = query.all()
        Subjects = [SubjectPersistanceAdapter.persistance_to_domain(Subject) for Subject in db_Subjects]
        return Subjects

    def create(self, subject: Subject) -> Subject:
        db_subject = SubjectPersistanceAdapter.domain_to_persistance(subject)
        self.session.add(db_subject)
        self.session.commit()
        self.session.refresh(db_subject)
        subject = SubjectPersistanceAdapter.persistance_to_domain(db_subject)
        return subject
