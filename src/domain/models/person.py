from dataclasses import dataclass

from .address import Address
from .value_objects import PhoneNumber, Name, Email


@dataclass
class Person:
    email: Email
    first_name: Name
    last_name: Name
    phone_number: PhoneNumber
    address: Address
