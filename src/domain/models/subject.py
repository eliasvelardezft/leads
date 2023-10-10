from dataclasses import dataclass

from .value_objects import Name


@dataclass
class Subject:
    name: Name
    description: str
