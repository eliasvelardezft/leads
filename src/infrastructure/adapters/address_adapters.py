from domain.interfaces.adapters import IClientAdapter, IPersistanceAdapter
from domain.models.address import Address
from infrastructure.db.models import AddressSQL
from api.v1.dtos.address import AddressCreate, AddressRead


class AddressPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(address: Address) -> AddressSQL:
        return AddressSQL(
            **address.dict(),
        )
    
    @staticmethod
    def persistance_to_domain(address: AddressSQL) -> Address:
        return Address(
            **address.dict(),
        )


class AddressClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(address: AddressCreate) -> Address:
        return Address(
            **address.dict(),
        )
    
    @staticmethod
    def domain_to_client(address: Address) -> AddressRead:
        return AddressRead(
            **address.dict(),
        )
