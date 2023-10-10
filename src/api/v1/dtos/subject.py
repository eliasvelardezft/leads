from pydantic import BaseModel, validator

from domain.models.value_objects import Name


class SubjectBase(BaseModel):
    name: str
    description: str

    @validator("name")
    def name_validator(cls, value: str) -> str:
        return Name(name=value).name


class SubjectCreate(SubjectBase):
    pass


class SubjectRead(SubjectBase):
    id: int

    class Config:
        from_attributes = True


class SubjectUpdate(SubjectBase):
    name: str | None = None
    description: str | None = None
