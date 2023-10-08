from dataclasses import dataclass


@dataclass
class Address:
    street: str
    number: int
    city: str
    province: str
