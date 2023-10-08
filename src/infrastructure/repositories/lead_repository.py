from domain.interfaces import IRepository

# TODO: implement real repository with sqlalchemy
from collections import namedtuple
FakeLead = namedtuple("Lead", ["id", "first_name", "last_name", "email"])


class LeadRepository(IRepository):
    leads = [
        FakeLead(
            id=1,
            first_name="Lionel",
            last_name="Messi",
            email="lio.messi@gmail.com",
        ),
        FakeLead(
            id=2,
            first_name="Cristiano",
            last_name="Ronaldo",
            email="cristiano.ronaldo@gmail.com",
        )
    ]

    def get(self, id: str):
        return filter(lambda lead: lead["id"] == id, self.leads)

    def get_all(self):
        return self.leads

    def create(self, lead):
        lead.id = len(self.leads) + 1
        self.leads.append(lead)
        return lead
