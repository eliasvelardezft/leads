from dataclasses import dataclass
from datetime import datetime

from .subject import Subject


@dataclass
class Course:
    subject: Subject
    start_date: datetime
    end_date: datetime
    professor: str
    classroom: str

    id: str | None = None
    created_date: str | None = None
    updated_date: str | None = None
    deleted_date: str | None = None
