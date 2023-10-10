from dataclasses import dataclass, field

from .subject import Subject
from .value_objects import Name


@dataclass
class Career:
    name: Name
    description: str
    subjects: list[Subject] = field(default_factory=list)
