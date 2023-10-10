from dataclasses import dataclass


@dataclass
class AddressSQL:
    id: str
    street: str
    number: int
    city: str
    province: str
    country: str
