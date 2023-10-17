from pydantic import BaseModel, field_validator

from .subject import SubjectRead
from domain.models.value_objects import Name


class CareerBase(BaseModel):
    name: str
    description: str
    subject_ids: list[int] | None = []

    @field_validator("name")
    def name_validator(cls, value: str) -> str:
        return Name(name=value).name


class CareerCreate(CareerBase):
    pass

class CareerRead(CareerBase):
    id: int
    subject_ids: list[int] | None = []


    model_config = {
        "from_attributes": True
    }


class CareerUpdate(CareerBase):
    name: str | None = None
    description: str | None = None
