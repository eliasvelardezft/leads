from abc import ABC


class IRepository(ABC):
    def get(id: str):
        raise NotImplementedError

    def get_all():
        raise NotImplementedError
