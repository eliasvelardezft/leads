from dataclasses import dataclass
from datetime import date

from .subject import Subject


@dataclass
class Course:
    start_date: date
    end_date: date
    professor: str
    classroom: str

    subject: Subject | None = None
    subject_id: str | None = None
    id: str | None = None
    created_date: str | None = None
    updated_date: str | None = None
    deleted_date: str | None = None
