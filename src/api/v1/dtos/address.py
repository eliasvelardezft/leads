from pydantic import BaseModel


class AddressBase(BaseModel):
    street: str
    number: int
    city: str
    province: str
    country: str


class AddressCreate(AddressBase):
    pass


class AddressRead(AddressBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class AddressUpdate(AddressBase):
    street: str | None = None
    number: str | None = None
    city: str | None = None
    province: str | None = None
    country: str | None = None
