from datetime import datetime

from pydantic import BaseModel, Field


class PhoneNumber(BaseModel):
    number: str = Field(regex=r"^\+\d{1,3}\d{1,14}$")


class Name(BaseModel):
    name: str = Field(min_length=1, max_length=50)


class Year(BaseModel):
    year: int = Field(ge=1918, le=datetime.now().year)
