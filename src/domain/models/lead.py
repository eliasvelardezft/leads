from dataclasses import dataclass

from .career import Career
from .person import Person
from .value_objects import Year

@dataclass
class Lead(Person):
    id: int | None = None
    career: Career
    year_of_inscription: Year