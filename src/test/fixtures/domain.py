import pytest
from datetime import datetime

from domain.models import Career, Subject, Course, Enrollment, Lead, Address, StatusChange, CreatedStatus
from domain.models.value_objects import Name, Email, PhoneNumber, Year


@pytest.fixture
def domain_career():
    return Career(
        id=1,
        name=Name(name='Software Engineering'),
        description='Develops software applications and systems',
        subject_ids=[1, 2, 3]
    )

@pytest.fixture
def domain_subject():
    return Subject(
        id=1,
        name=Name(name='Mathematics'),
        description='The study of numbers and their properties',
    )

@pytest.fixture
def domain_course(domain_subject):
    return Course(
        id=1,
        subject_id=1,
        start_date=datetime.strptime('2024-03-16', '%Y-%m-%d').date(),
        end_date=datetime.strptime('2024-06-16', '%Y-%m-%d').date(),
        professor='Bill gates',
        classroom='404',
        subject=domain_subject,
    )

@pytest.fixture
def domain_address():
    return Address(
        id=1,
        street='Av. Colon',
        number=100,
        city='Cordoba',
        province='Cordoba',
        country='Argentina',
    )

@pytest.fixture
def domain_lead(domain_career, domain_address):
    return Lead(
        id=1,
        first_name=Name(name='Lionel'),
        last_name=Name(name='Messi'),
        year_of_inscription=Year(year=2021),
        email=Email(email="liomessi@gmail.com"),
        phone_number=PhoneNumber(number="+1234567890"),
        address=domain_address,
        career=domain_career,
        career_id=domain_career.id,
    )

@pytest.fixture
def domain_enrollment(domain_lead, domain_course):
    return Enrollment(
        id=1,
        subject_times_taken=1,
        lead_id=1,
        course_id=1,
        # status_changes=[],
        lead=domain_lead,
        course=domain_course
    )

@pytest.fixture
def domain_status_change():
    return StatusChange(
        id=1,
        start_date=datetime.strptime('2022-01-01', '%Y-%m-%d'),
        end_date=datetime.strptime('2022-01-31', '%Y-%m-%d'),
        status=CreatedStatus(),
    )
