from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .address import AddressSQL
from infrastructure.persistance.base import SQLBaseModel


class PersonSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)

    address_id: Mapped[int] = mapped_column(Integer, ForeignKey("address.id"))
    address: Mapped[AddressSQL] = relationship("AddressSQL")
