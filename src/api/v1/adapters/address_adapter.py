from dataclasses import asdict

from api.v1.dtos.address import AddressCreate, AddressRead
from domain.interfaces import IClientAdapter
from domain.models import Address


class AddressClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(address: AddressCreate) -> Address:
        return Address(
            **address.model_dump(),
        )
    
    @staticmethod
    def domain_to_client(address: Address) -> AddressRead:
        return AddressRead(
            **asdict(address),
        )
