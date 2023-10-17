from datetime import datetime

from api.v1.adapters import (
    CareerClientAdapter,
    CourseClientAdapter,
    EnrollmentClientAdapter,
    LeadClientAdapter,
    StatusChangeClientAdapter,
    StatusClientAdapter,
    SubjectClientAdapter
)
from infrastructure.persistance.adapters import (
    CareerPersistanceAdapter,
    CoursePersistanceAdapter,
    EnrollmentPersistanceAdapter,
    LeadPersistanceAdapter,
    StatusChangePersistanceAdapter,
    StatusPersistanceAdapter,
    SubjectPersistanceAdapter,
)
from infrastructure.persistance.models import (
    CareerSQL,
    CourseSQL,
    EnrollmentSQL,
    LeadSQL,
    StatusChangeSQL,
    SubjectSQL,
)
from api.v1.adapters.address_adapter import AddressClientAdapter
from api.v1.dtos.address import AddressCreate
from api.v1.dtos.career import CareerCreate, CareerRead
from api.v1.dtos.course import CourseCreate, CourseRead
from api.v1.dtos.enrollment import EnrollmentCreate, EnrollmentRead
from api.v1.dtos.lead import LeadCreate, LeadRead
from api.v1.dtos.status import StatusChangeRead
from api.v1.dtos.subject import SubjectCreate, SubjectRead
from domain.interfaces import IStatus
from domain.models.career import Career
from domain.models.course import Course
from domain.models.enrollment import Enrollment
from domain.models.lead import Lead
from domain.models.status import CreatedStatus, EnrollmentStatus, StatusChange
from domain.models.subject import Subject
from domain.models.value_objects import Email, Name, PhoneNumber, Year
from domain.services import EnrollmentService, LeadService, AdminService
from test.conftest import BaseTestClass


class TestAdapters(BaseTestClass):
    def test_career_client_adapter(self, test_session):
        subjects = self._generate_subjects()
        subject_ids = [subject.id for subject in subjects] 

        career_create = CareerCreate(
            name='Software Engineering',
            description='Develops software applications and systems',
            subject_ids=subject_ids
        )
        career = CareerClientAdapter.client_to_domain(career_create)
        assert isinstance(career, Career)
        assert career.name == Name(name='Software Engineering')
        assert career.description == 'Develops software applications and systems'
        assert career.subject_ids == subject_ids

        career_persistance = CareerPersistanceAdapter.domain_to_persistance(career)
        assert isinstance(career_persistance, CareerSQL)
        assert career_persistance.name == 'Software Engineering'
        assert career_persistance.description == 'Develops software applications and systems'
        assert career_persistance.subject_ids == subject_ids

        test_session.add(career_persistance)
        test_session.commit()
        test_session.refresh(career_persistance)

        domain_career = CareerPersistanceAdapter.persistance_to_domain(career_persistance)

        assert isinstance(domain_career, Career)
        assert domain_career.id == career_persistance.id
        assert domain_career.name == Name(name='Software Engineering')
        assert domain_career.description == 'Develops software applications and systems'
        assert domain_career.subject_ids == subject_ids

        career_read = CareerClientAdapter.domain_to_client(domain_career)
        assert isinstance(career_read, CareerRead)
        assert career_read.id == 1
        assert career_read.name == 'Software Engineering'
        assert career_read.description == 'Develops software applications and systems'
        assert career_read.subject_ids == subject_ids

    def test_subject_client_adapter(self, test_session):
        subject_create = SubjectCreate(
            name='Mathematics',
            description='The study of numbers and their properties',
        )
        subject = SubjectClientAdapter.client_to_domain(subject_create)
        assert isinstance(subject, Subject)
        assert subject.name == Name(name='Mathematics')
        assert subject.description == 'The study of numbers and their properties'

        subject_persistance = SubjectPersistanceAdapter.domain_to_persistance(subject)
        assert isinstance(subject_persistance, SubjectSQL)
        assert subject_persistance.name == 'Mathematics'
        assert subject_persistance.description == 'The study of numbers and their properties'

        test_session.add(subject_persistance)
        test_session.commit()
        test_session.refresh(subject_persistance)

        domain_subject = SubjectPersistanceAdapter.persistance_to_domain(subject_persistance)
        assert isinstance(domain_subject, Subject)
        assert domain_subject.id == subject_persistance.id
        assert domain_subject.name == Name(name='Mathematics')
        assert domain_subject.description == 'The study of numbers and their properties'

        subject_read = SubjectClientAdapter.domain_to_client(domain_subject)
        assert isinstance(subject_read, SubjectRead)
        assert subject_read.id == 1
        assert subject_read.name == 'Mathematics'
        assert subject_read.description == 'The study of numbers and their properties'

    def test_course_client_adapter(self, test_session):
        self._generate_subjects()

        course_create = CourseCreate(
            subject_id=1,
            start_date='2024-03-16',
            end_date='2024-06-16',
            professor='Bill gates',
            classroom='404'
        )
        course = CourseClientAdapter.client_to_domain(course_create)
        assert isinstance(course, Course)
        assert course.subject_id == 1
        assert course.start_date.year == 2024
        assert course.start_date.month == 3
        assert course.start_date.day == 16
        assert course.end_date.year == 2024
        assert course.end_date.month == 6
        assert course.end_date.day == 16
        assert course.professor == 'Bill gates'
        assert course.classroom == '404'

        course_persistance = CoursePersistanceAdapter.domain_to_persistance(course)
        assert isinstance(course_persistance, CourseSQL)
        assert course_persistance.subject_id == 1
        assert course_persistance.start_date == datetime.strptime('2024-03-16', '%Y-%m-%d').date()
        assert course_persistance.end_date == datetime.strptime('2024-06-16', '%Y-%m-%d').date()
        assert course_persistance.professor == 'Bill gates'
        assert course_persistance.classroom == '404'

        test_session.add(course_persistance)
        test_session.commit()
        test_session.refresh(course_persistance)

        domain_course = CoursePersistanceAdapter.persistance_to_domain(course_persistance)
        assert isinstance(domain_course, Course)
        assert domain_course.id == course_persistance.id
        assert domain_course.subject_id == 1
        assert domain_course.start_date.year == 2024
        assert domain_course.start_date.month == 3
        assert domain_course.start_date.day == 16
        assert domain_course.end_date.year == 2024
        assert domain_course.end_date.month == 6
        assert domain_course.end_date.day == 16
        assert domain_course.professor == 'Bill gates'
        assert domain_course.classroom == '404'

        course_read = CourseClientAdapter.domain_to_client(domain_course)
        assert isinstance(course_read, CourseRead)
        assert course_read.id == 1
        assert course_read.subject_id == 1
        assert course_read.start_date == datetime.strptime('2024-03-16', '%Y-%m-%d').date()
        assert course_read.end_date == datetime.strptime('2024-06-16', '%Y-%m-%d').date()
        assert course_read.professor == 'Bill gates'
        assert course_read.classroom == '404'

    def test_enrollment_client_adapter(self, test_session):
        self._generate_lead()
        subjects = self._generate_subjects()
        self._generate_career(subjects)
        self._generate_course(subjects[0])

        enrollment_create = EnrollmentCreate(
            subject_times_taken=1,
            lead_id=1,
            course_id=1,
        )
        enrollment = EnrollmentClientAdapter.client_to_domain(enrollment_create)
        assert isinstance(enrollment, Enrollment)
        assert enrollment.subject_times_taken == 1
        assert enrollment.lead_id == 1
        assert enrollment.course_id == 1
        assert len(enrollment.status_changes) == 1

        enrollment_persistance = EnrollmentPersistanceAdapter.domain_to_persistance(enrollment)
        assert isinstance(enrollment_persistance, EnrollmentSQL)
        assert enrollment_persistance.subject_times_taken == 1
        assert enrollment_persistance.lead_id == 1
        assert enrollment_persistance.course_id == 1

        test_session.add(enrollment_persistance)
        test_session.commit()
        test_session.refresh(enrollment_persistance)

        domain_enrollment = EnrollmentPersistanceAdapter.persistance_to_domain(enrollment_persistance)
        assert isinstance(domain_enrollment, Enrollment)
        assert domain_enrollment.id == enrollment_persistance.id
        assert domain_enrollment.subject_times_taken == 1
        assert domain_enrollment.lead_id == 1
        assert domain_enrollment.course_id == 1

        enrollment_read = EnrollmentClientAdapter.domain_to_client(domain_enrollment)
        assert isinstance(enrollment_read, EnrollmentRead)
        assert enrollment_read.id == 1
        assert enrollment_read.subject_times_taken == 1
        assert enrollment_read.lead_id == 1
        assert enrollment_read.course_id == 1

    def test_lead_client_adapter(self, test_session):
        subjects = self._generate_subjects()
        self._generate_career(subjects)

        address_create = AddressCreate(
            street='Av. Colon',
            number=100,
            city='Cordoba',
            province='Cordoba',
            country='Argentina',
        )
        lead_create = LeadCreate(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone_number='+1234567890',
            address=address_create,
            career_id=1,
            year_of_inscription=2022
        )
        lead = LeadClientAdapter.client_to_domain(lead_create)
        assert isinstance(lead, Lead)
        assert lead.first_name == Name(name='John')
        assert lead.last_name == Name(name='Doe')
        assert lead.email == Email(email='john.doe@example.com')
        assert lead.phone_number == PhoneNumber(number='+1234567890')
        assert lead.career_id == 1
        assert lead.year_of_inscription == Year(year=2022)

        lead_persistance = LeadPersistanceAdapter.domain_to_persistance(lead)
        assert isinstance(lead_persistance, LeadSQL)
        assert lead_persistance.first_name == lead.first_name.name
        assert lead_persistance.last_name == lead.last_name.name
        assert lead_persistance.email == lead.email.email
        assert lead_persistance.phone_number == lead.phone_number.number
        assert lead_persistance.year_of_inscription == lead.year_of_inscription.year

        test_session.add(lead_persistance)
        test_session.commit()
        test_session.refresh(lead_persistance)

        domain_lead = LeadPersistanceAdapter.persistance_to_domain(lead_persistance)
        assert isinstance(domain_lead, Lead)
        assert domain_lead.id == lead_persistance.id
        assert domain_lead.first_name == Name(name='John')
        assert domain_lead.last_name == Name(name='Doe')
        assert domain_lead.email == Email(email="john.doe@example.com")
        assert domain_lead.phone_number == PhoneNumber(number="+1234567890")
        assert domain_lead.year_of_inscription == Year(year=2022)

        lead_read = LeadClientAdapter.domain_to_client(domain_lead)
        address_read = AddressClientAdapter.domain_to_client(domain_lead.address)
        assert isinstance(lead_read, LeadRead)
        assert lead_read.id == 1
        assert lead_read.first_name == domain_lead.first_name.name
        assert lead_read.last_name == domain_lead.last_name.name
        assert lead_read.email == domain_lead.email.email
        assert lead_read.phone_number == domain_lead.phone_number.number
        assert lead_read.year_of_inscription == domain_lead.year_of_inscription.year
        assert lead_read.career_id == 1
        assert lead_read.address == address_read

    def test_status_change_client_adapter(self, test_session):
        self._generate_support_objects()
        self._generate_enrollment()

        status_change_persistance = test_session.query(StatusChangeSQL).first()

        domain_status_change = StatusChangePersistanceAdapter.persistance_to_domain(status_change_persistance)
        assert isinstance(domain_status_change, StatusChange)
        assert domain_status_change.id == status_change_persistance.id
        assert domain_status_change.status == CreatedStatus()
        
        status_change_read = StatusChangeClientAdapter.domain_to_client(domain_status_change)
        assert isinstance(status_change_read, StatusChangeRead)
        assert status_change_read.id == 1
        assert status_change_read.status == EnrollmentStatus.CREATED

    def test_status_client_adapter(self):
        status_data = EnrollmentStatus.CREATED
        new_status = StatusClientAdapter.client_to_domain(status_data)
        assert isinstance(new_status, IStatus)
        assert new_status.status == EnrollmentStatus.CREATED

        status_read = StatusClientAdapter.domain_to_client(new_status)
        assert status_read == EnrollmentStatus.CREATED
    
        status_persistance = StatusPersistanceAdapter.domain_to_persistance(new_status)
        assert status_persistance == EnrollmentStatus.CREATED
