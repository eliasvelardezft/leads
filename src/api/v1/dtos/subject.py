from pydantic import BaseModel, field_validator

from domain.models.value_objects import Name


class SubjectBase(BaseModel):
    name: str
    description: str

    @field_validator("name")
    def name_validator(cls, value: str) -> str:
        return Name(name=value).name


class SubjectCreate(SubjectBase):
    pass


class SubjectRead(SubjectBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class SubjectUpdate(SubjectBase):
    name: str | None = None
    description: str | None = None
