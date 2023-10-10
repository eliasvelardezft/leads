from dataclasses import dataclass


@dataclass
class Address:
    street: str
    number: int
    city: str
    province: str
    country: str

    id: str | None = None
    created_date: str | None = None
    updated_date: str | None = None
    deleted_date: str | None = None
