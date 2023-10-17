import pytest

from sqlalchemy.orm import Session

from api.v1.dependencies.domain_services import (
    get_lead_service,
    get_enrollment_service,
)
from domain.services import LeadService, EnrollmentService


@pytest.fixture(scope="function")
def test_lead_service(test_session: Session) -> LeadService:
    return get_lead_service(test_session)


@pytest.fixture(scope="function")
def test_enrollment_service(test_session: Session) -> EnrollmentService:
    return get_enrollment_service(test_session)
