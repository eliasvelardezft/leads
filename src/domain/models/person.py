from dataclasses import dataclass

from pydantic import EmailStr

from .address import Address
from .value_objects import PhoneNumber, Name


@dataclass
class Person:
    first_name: Name
    last_name: Name
    email: EmailStr
    phone_number: PhoneNumber
    address: Address