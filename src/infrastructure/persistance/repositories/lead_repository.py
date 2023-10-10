from domain.interfaces import IRepository
from infrastructure.persistance.adapters import LeadPersistanceAdapter
from domain.models import Lead


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

    def get(self, id: str) -> Lead:
        db_lead = filter(lambda lead: lead["id"] == id, self.leads)
        lead = LeadPersistanceAdapter.persistance_to_domain(db_lead)
        return lead

    def get_all(self) -> list[Lead]:
        leads = [
            LeadPersistanceAdapter.persistance_to_domain(lead)
            for lead in self.leads
        ]
        return leads

    def create(self, lead: Lead) -> Lead:
        db_lead = lead
        db_lead.id = len(self.leads) + 1
        self.leads.append(db_lead)
        lead = LeadPersistanceAdapter.persistance_to_domain(db_lead)
        return lead
