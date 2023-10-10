from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.persistance.base import SQLBaseModel


class AddressSQL(SQLBaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String)
    number: Mapped[int] = mapped_column(Integer)
    city: Mapped[str] = mapped_column(String)
    province: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)
