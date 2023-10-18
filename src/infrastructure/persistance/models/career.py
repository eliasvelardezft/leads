from sqlalchemy import String, Integer, ForeignKey, Table, Column
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistance.base import SQLBaseModel, Base


career_subject_association = Table(
    'career_subject_association',
    SQLBaseModel.metadata,
    Column('career_id', Integer, ForeignKey('career.id'), primary_key=True),
    Column('subject_id', Integer, ForeignKey('subject.id'), primary_key=True)
)


class CareerSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String)

    subjects = relationship(
        'SubjectSQL',
        secondary=career_subject_association,
        back_populates='careers',
        viewonly=True,
    )
    subject_associations: Mapped[list["SubjectAssociation"]] = relationship(
        "SubjectAssociation",
        back_populates="career",
        cascade="all, delete-orphan"
    )
    subject_ids: Mapped[list[int]] = association_proxy(
        "subject_associations",
        "subject_id",
        creator=lambda s_id: SubjectAssociation(subject_id=s_id),
    )


class SubjectAssociation(Base):
    __table__ = career_subject_association
    career: Mapped[CareerSQL] = relationship(
        CareerSQL,
        back_populates="subject_associations"
    )
