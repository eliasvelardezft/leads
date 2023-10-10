from sqlalchemy import Integer, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .person import PersonSQL
from .career import CareerSQL


class LeadSQL(PersonSQL):
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    year_of_inscription: Mapped[int] = mapped_column(Integer)
    
    career: Mapped[CareerSQL] = relationship("CareerSQL")
    career_id: Mapped[int] = mapped_column(Integer, ForeignKey("career.id"))

    enrollments: Mapped[list] = relationship("EnrollmentSQL", back_populates="lead")
