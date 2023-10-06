from dataclasses import dataclass

# from .subject import Subject
from .value_objects import Name


@dataclass
class Career:
    name: Name
    # subjects: list[Subject] = []
