from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistance.base import SQLBaseModel
from .career import career_subject_association


class SubjectSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String)

    careers = relationship(
        'CareerSQL',
        secondary=career_subject_association,
        back_populates='subjects',
        viewonly=True,
    )
