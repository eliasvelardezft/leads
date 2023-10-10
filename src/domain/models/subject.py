from dataclasses import dataclass

from .value_objects import Name


@dataclass
class Subject:
    name: Name
    description: str

    id: str | None = None
    created_date: str | None = None
    updated_date: str | None = None
    deleted_date: str | None = None
