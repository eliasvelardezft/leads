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
