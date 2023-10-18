import pytest
from datetime import datetime

from api.v1.dtos.address import AddressCreate
from api.v1.dtos.career import CareerCreate
from api.v1.dtos.course import CourseCreate
from api.v1.dtos.lead import LeadCreate
from api.v1.dtos.subject import SubjectCreate
from api.v1.dtos.enrollment import EnrollmentCreate


@pytest.fixture(scope="function")
def address_create() -> AddressCreate:
    return AddressCreate(
        street='Av. Colon',
        number=100,
        city='Cordoba',
        province='Cordoba',
        country='Argentina',
    )


@pytest.fixture(scope="function")
def career_create() -> CareerCreate:
    return CareerCreate(
        name='Ingenieria en Sistemas de Informacion',
        description='Ingenieria en Sistemas de Informacion',
        subject_ids=[],
    )


@pytest.fixture(scope="function")
def subject_create() -> SubjectCreate:
    return SubjectCreate(
        name='Algebra I',
        description='Algebra lineal',
    )


@pytest.fixture(scope="function")
def course_create() -> CourseCreate:
    return CourseCreate(
        subject_id=1,
        start_date=datetime.strptime('2024-03-16', '%Y-%m-%d').date(),
        end_date=datetime.strptime('2024-06-16', '%Y-%m-%d').date(),
        professor='Bill Gates',
        classroom='404',
    )


@pytest.fixture(scope="function")
def lead_create(address_create) -> LeadCreate:
    return LeadCreate(
        first_name='Lionel',
        last_name='Messi',
        email='liomessi@gmail.com',
        phone_number='1234567',
        address=address_create,
        year_of_inscription=2021,
        career_id=1,
    )


@pytest.fixture(scope="function")
def enrollment_create(lead_create, course_create):
    return EnrollmentCreate(
        subject_times_taken=1,
        lead_id=1,
        course_id=1,
    )