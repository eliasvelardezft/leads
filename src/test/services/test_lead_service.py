from dataclasses import replace

from domain.services import LeadService
from test.conftest import BaseTestClass


class TestLeadService(BaseTestClass):
    """
    def get_leads(
        self,
        filters: dict[str, Any] = {},
    ) -> list[Lead]:
        return self.repository.filter(filters=filters)

    def get_lead(self, id: str) -> Lead | None:
        return self.repository.get(id=id)
    """
    def test_create_lead(
        self,
        domain_lead,
        test_lead_service: LeadService,
    ):
        self._generate_support_objects()

        lead = test_lead_service.create_lead(
            domain_lead
        )

        assert lead.id == 1
        assert lead.first_name == domain_lead.first_name
        assert lead.last_name == domain_lead.last_name
        assert lead.email == domain_lead.email
        assert lead.phone_number == domain_lead.phone_number
        assert lead.career_id == domain_lead.career.id
        assert lead.year_of_inscription == domain_lead.year_of_inscription

    def test_get_leads(
        self,
        test_lead_service: LeadService
    ):
        self._generate_support_objects()
        self._generate_lead()
        self._generate_lead(id="2")

        leads = test_lead_service.get_leads(
            filters={
                "email": "charly.snm2@gmail.com"
            }
        )
        assert len(leads) == 1
        assert leads[0].id == 2
        assert leads[0].email.email == "charly.snm2@gmail.com"

    def test_get_lead(
        self,
        test_lead_service: LeadService
    ):
        self._generate_support_objects()
        self._generate_lead()

        lead = test_lead_service.get_lead(id="1")
        assert lead is not None
        assert lead.id == 1
