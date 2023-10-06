from pydantic import BaseModel, validator

from domain.models.value_objects import Email, Name


class LeadBase(BaseModel):
    first_name: str
    last_name: str
    email: str

    @validator("email")
    def email_validator(cls, value: str) -> str:
        return Email(email=value).email

    @validator("first_name", "last_name")
    def name_validator(cls, value: str) -> str:
        return Name(name=value).name


class LeadCreate(LeadBase):
    pass


class LeadRead(LeadBase):
    id: int

    class Config:
        orm_mode = True


class LeadUpdate(LeadBase):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
