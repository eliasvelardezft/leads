from dataclasses import asdict

from domain.interfaces.adapters import IPersistanceAdapter
from domain.models.address import Address
from infrastructure.persistance.models import AddressSQL


class AddressPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(address: Address) -> AddressSQL:
        return AddressSQL(
            **asdict(address),
        )
    
    @staticmethod
    def persistance_to_domain(address: AddressSQL) -> Address:
        return Address(
            **address.as_dict(),
        )
