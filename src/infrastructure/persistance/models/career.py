from sqlalchemy import String, Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistance.base import SQLBaseModel


career_subject_association = Table(
    'career_subject_association',
    SQLBaseModel.metadata,
    Column('career_id', Integer, ForeignKey('career.id')),
    Column('subject_id', Integer, ForeignKey('subject.id'))
)


class CareerSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String)

    subjects = relationship(
        'SubjectSQL',
        secondary=career_subject_association,
        back_populates='careers'
    )
