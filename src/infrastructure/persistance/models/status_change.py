from sqlalchemy import DateTime, Enum, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .enrollment import EnrollmentSQL
from infrastructure.persistance.base import SQLBaseModel


class StatusChangeSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[DateTime] = mapped_column(DateTime)
    end_date: Mapped[DateTime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(
        Enum(
            "created",
            "progress",
            "completed",
            "failed",
            "dropped",
            name="enrollment_status_enum"
        )
    )

    enrollment_id: Mapped[int] = mapped_column(Integer, ForeignKey("enrollment.id"))
    enrollment: Mapped[EnrollmentSQL] = relationship(
        "EnrollmentSQL",
        back_populates="status_changes"
    )
