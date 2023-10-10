from datetime import datetime

from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistance.base import SQLBaseModel
from .subject import SubjectSQL

class CourseSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[datetime] = mapped_column(DateTime)
    professor: Mapped[str] = mapped_column(String)
    classroom: Mapped[str] = mapped_column(String)

    subject: Mapped[SubjectSQL] = relationship("SubjectSQL")
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subject.id"))

    enrollments: Mapped[list] = relationship("EnrollmentSQL", back_populates="course")
