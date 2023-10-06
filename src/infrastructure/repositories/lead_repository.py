from domain.interfaces import IRepository


class LeadRepository(IRepository):
    def get(self, id: str):
        pass

    def get_all(self):
        pass

    def create(self, lead):
        pass