from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .lead import LeadSQL
from .course import CourseSQL
from infrastructure.persistance.base import SQLBaseModel


class EnrollmentSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    subject_times_taken: Mapped[int] = mapped_column(Integer)
    
    lead_id: Mapped[int] = mapped_column(Integer, ForeignKey("lead.id"))
    lead: Mapped[LeadSQL] = relationship("LeadSQL", back_populates="enrollments")
    
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey("course.id"))
    course: Mapped[CourseSQL] = relationship("CourseSQL", back_populates="enrollments")

    status_changes: Mapped[list] = relationship("StatusChangeSQL", back_populates="enrollment")
