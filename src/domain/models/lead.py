from dataclasses import dataclass

from .career import Career
from .person import Person
from .value_objects import Year

@dataclass
class Lead(Person):
    year_of_inscription: Year
    career: Career | None = None
    career_id: int | None = None
    id: int | None = None