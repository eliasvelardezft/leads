from dataclasses import dataclass


from .career import Career
from .value_objects import Name


@dataclass
class Subject:
    name: Name
    career: Career
