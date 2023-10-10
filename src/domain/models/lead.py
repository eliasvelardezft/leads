from dataclasses import dataclass

from .career import Career
from .person import Person
from .value_objects import Year

@dataclass
class Lead(Person):
    year_of_inscription: Year
    career: Career | None = None
    career_id: int | None = None

    id: str | None = None
    created_date: str | None = None
    updated_date: str | None = None
    deleted_date: str | None = None
