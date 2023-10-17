from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from sqlalchemy.orm import Session
from api.v1.routers.lead import router
from api.v1.dtos.lead import LeadCreate
from domain.models.lead import Lead
from domain.services import LeadService
from api.v1.adapters import LeadClientAdapter
from api.v1.exceptions import EntityAlreadyExists
from test.conftest import BaseTestClass


class TestLeadRouter(BaseTestClass):
    def test_create_lead(self, client, lead_create):
        self._generate_support_objects()

        response = client.post('/api/v1/leads', json=lead_create.model_dump())
        assert response.status_code == 201
        assert response.json() == 1

        response = client.post('/api/v1/leads', json=lead_create.model_dump())
        assert response.status_code == 409
        assert response.json() == {'detail': 'entity_already_exists'}

    def test_get_lead(self, client, lead_create):
        self._generate_support_objects()

        client.post('/api/v1/leads', json=lead_create.model_dump())

        response = client.get('/api/v1/leads/1')
        assert response.status_code == 200

    def test_get_leads(self, client, lead_create):
        self._generate_support_objects()

        second_lead = lead_create.model_copy()
        second_lead.email = 'second@gmail.com'

        client.post('/api/v1/leads', json=lead_create.model_dump())
        client.post('/api/v1/leads', json=second_lead.model_dump())

        response = client.get('/api/v1/leads')
        assert response.status_code == 200

        response_first = response.json()[0]
        response_second = response.json()[1]

        assert response_first['email'] == lead_create.email
        assert response_second['email'] == second_lead.email
