import pytest

from infrastructure.persistance.repositories import EnrollmentRepository


@pytest.fixture(scope="function")
def test_enrollment_repository(test_session) -> EnrollmentRepository:
    return EnrollmentRepository(test_session)
