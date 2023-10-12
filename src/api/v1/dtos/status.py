from datetime import datetime

from pydantic import BaseModel

from domain.models.status import EnrollmentStatus


class StatusChangeBase(BaseModel):
    start_date: datetime
    end_date: datetime | None = None
    status: EnrollmentStatus


class StatusChangeRead(StatusChangeBase):
    id: int

    class Config:
        from_attributes = True
