from pydantic import BaseModel


class AddressBase(BaseModel):
    street: str
    number: str
    city: str
    state: str
    country: str


class AddressCreate(AddressBase):
    pass


class AddressRead(AddressBase):
    id: int

    class Config:
        from_attributes = True


class AddressUpdate(AddressBase):
    street: str | None = None
    number: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None