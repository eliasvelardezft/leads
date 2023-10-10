from pydantic import BaseModel, validator

from domain.models.value_objects import Name


class CareerBase(BaseModel):
    name: str
    description: str

    @validator("name")
    def name_validator(cls, value: str) -> str:
        return Name(name=value).name


class CareerCreate(CareerBase):
    pass


class CareerRead(CareerBase):
    id: int

    class Config:
        from_attributes = True


class CareerUpdate(CareerBase):
    name: str | None = None
    description: str | None = None
