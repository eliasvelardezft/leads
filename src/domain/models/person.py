from dataclasses import dataclass

from .address import Address
from .value_objects import PhoneNumber, Name, Email


@dataclass
class Person:
    first_name: Name
    last_name: Name
    email: Email
    phone_number: PhoneNumber | None = None
    address: Address | None = None