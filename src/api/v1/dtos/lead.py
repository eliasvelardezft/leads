from pydantic import BaseModel, validator

from .address import AddressCreate, AddressRead
from .career import CareerRead
from domain.models.value_objects import Email, Name, PhoneNumber, Year


class LeadBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    phone_number: str
    address: AddressCreate
    career_id: int
    year_of_inscription: int

    @validator("email")
    def email_validator(cls, value: str) -> str:
        return Email(email=value).email

    @validator("first_name", "last_name")
    def name_validator(cls, value: str) -> str:
        return Name(name=value).name

    @validator("phone_number")
    def phone_number_validator(cls, value: str) -> str:
        return PhoneNumber(number=value).number

    @validator("year_of_inscription")
    def year_of_inscription_validator(cls, value: int) -> int:
        return Year(year=value).year


class LeadCreate(LeadBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "eliasvelardez@gmail.com",
                    "first_name": "elias",
                    "last_name": "velardez",
                    "phone_number": "+541234567",
                    "address": {
                        "street": "au",
                        "number": "40",
                        "city": "cba",
                        "state": "cba",
                        "country": "arg"
                    },
                    "career_id": 0,
                    "year_of_inscription": 1918
                }
            ]
        }
    }


class LeadRead(LeadBase):
    id: int
    address: AddressRead
    career: CareerRead

    class Config:
        from_attributes = True


class LeadUpdate(LeadBase):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    address: AddressCreate | None = None
    career_id: int | None = None
    year_of_inscription: int | None = None

