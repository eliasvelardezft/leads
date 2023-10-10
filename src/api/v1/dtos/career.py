from pydantic import BaseModel, validator

from .subject import SubjectRead
from domain.models.value_objects import Name


class CareerBase(BaseModel):
    name: str
    description: str
    subject_ids: list[int] | None = []

    @validator("name")
    def name_validator(cls, value: str) -> str:
        return Name(name=value).name


class CareerCreate(CareerBase):
    pass

class CareerRead(CareerBase):
    id: int
    subject_ids: list[SubjectRead] | None = []


    class Config:
        from_attributes = True


class CareerUpdate(CareerBase):
    name: str | None = None
    description: str | None = None
