from datetime import datetime, date

from pydantic import BaseModel, validator

from .subject import SubjectRead


class CourseBase(BaseModel):
    subject_id: int
    start_date: date
    end_date: date
    professor: str
    classroom: str

    @validator("start_date", "end_date")
    def date_validator(cls, value: date) -> date:
        if value < date.today():
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
    start_date: date | None = None
    end_date: date | None = None
    professor: str | None = None
    classroom: str | None = None
