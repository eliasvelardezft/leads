from datetime import datetime

from pydantic import BaseModel, validator

from .subject import SubjectRead


class CourseBase(BaseModel):
    subject_id: int
    start_date: datetime
    end_date: datetime
    professor: str
    classroom: str

    @validator("start_date", "end_date")
    def date_validator(cls, value: datetime) -> datetime:
        if value < datetime.now():
            raise ValueError("Date must be greater than now")
        return value


class CourseCreate(CourseBase):
    pass


class CourseRead(CourseBase):
    id: int
    subject: SubjectRead

    class Config:
        from_attributes = True


class CourseUpdate(CourseBase):
    subject_id: int | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    professor: str | None = None
    classroom: str | None = None
