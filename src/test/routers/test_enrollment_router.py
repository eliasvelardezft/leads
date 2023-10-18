
import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

from api.v1.routers.enrollment import router
from api.v1.dtos.enrollment import EnrollmentCreate
from domain.models.enrollment import Enrollment
from domain.services import EnrollmentService
from api.v1.adapters import EnrollmentClientAdapter
from api.v1.exceptions import EntityAlreadyExists
from test.conftest import BaseTestClass


class TestEnrollmentRouter(BaseTestClass):
    def test_create_enrollment(self, client, enrollment_create):
        self._generate_support_objects()
        self._generate_lead()

        response = client.post('/api/v1/enrollments', json=enrollment_create.model_dump())
        assert response.status_code == 201
        assert response.json()['id'] == 1

    def test_create_enrollment_bulk(self, client, enrollment_create):
        self._generate_support_objects()
        self._generate_lead()
        self._generate_lead(id=2)

        enrollment1 = enrollment_create

        enrollment2 = enrollment_create.model_copy()
        enrollment2.subject_times_taken = 2
        enrollment2.lead_id = 2

        response = client.post('/api/v1/enrollments/bulk', json=[enrollment1.model_dump(), enrollment2.model_dump()])
        enrollments = response.json()
        assert response.status_code == 201
        assert len(enrollments) == 2
        assert enrollments[0]['id'] == 1

        
    def test_get_enrollments(self, client: TestClient, enrollment_create):
        self._generate_support_objects()

        response = client.get('/api/v1/enrollments/1')
        assert response.status_code == 404
        assert response.json()['detail'] == 'entity_does_not_exist'

        self._generate_lead()
        self._generate_lead(id="2")
        
        enrollment1 = enrollment_create

        enrollment2 = enrollment_create.model_copy()
        enrollment2.subject_times_taken = 2
        enrollment2.lead_id = 2

        response = client.post('/api/v1/enrollments', json=enrollment1.model_dump())
        response = client.post('/api/v1/enrollments', json=enrollment2.model_dump())

        response = client.get('/api/v1/enrollments')
        assert response.status_code == 200
        enrollments = response.json()
        assert len(enrollments) == 2
        assert enrollments[0]['id'] == 1
        assert enrollments[0]['subject_times_taken'] == enrollment1.subject_times_taken
        assert enrollments[0]['lead_id'] == enrollment1.lead_id
        assert enrollments[0]['course_id'] == enrollment1.course_id
        assert enrollments[1]['id'] == 2
        assert enrollments[1]['subject_times_taken'] == enrollment2.subject_times_taken
        assert enrollments[1]['lead_id'] == enrollment2.lead_id
        assert enrollments[1]['course_id'] == enrollment2.course_id

        response = client.get('/api/v1/enrollments?lead_email=test@example.com')
        # assert response.status_code == 200
        enrollments = response.json()
        assert len(enrollments) == 0

        response = client.get(f'/api/v1/enrollments?lead_id={enrollment1.lead_id}')
        assert response.status_code == 200
        enrollments = response.json()
        assert len(enrollments) == 1
        assert enrollments[0]['id'] == 1
        assert enrollments[0]['subject_times_taken'] == enrollment1.subject_times_taken
        assert enrollments[0]['lead_id'] == enrollment1.lead_id
        assert enrollments[0]['course_id'] == enrollment1.course_id
