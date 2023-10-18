import pytest
from datetime import datetime

from sqlalchemy.orm import Session

from infrastructure.persistance.models import (
    SubjectSQL,
    CareerSQL,
    CourseSQL,
    LeadSQL,
    AddressSQL,
)
from infrastructure.persistance.adapters import EnrollmentPersistanceAdapter
from domain.models import Enrollment


class BaseTestClass:
    def _generate_subjects(self):
        test_session = self.session
        subjects_sql = [
            SubjectSQL(
                name='Algebra I',
                description='Algebra lineal',
            ),
            SubjectSQL(
                name='Analisis matematico II',
                description='Limites, integrales y derivadas',
            ),
        ]
        test_session.add_all(subjects_sql)
        test_session.commit()
        for subject in subjects_sql:
            test_session.refresh(subject)
        return subjects_sql

    def _generate_career(self, subjects_sql):
        test_session = self.session
        career_sql = CareerSQL(
            name='Ingenieria en Sistemas de Informacion',
            description='Ingenieria en Sistemas de Informacion',
            subject_ids=[subject.id for subject in subjects_sql],
        )
        test_session.add(career_sql)
        test_session.commit()
        test_session.refresh(career_sql)
        return career_sql

    def _generate_course(self, subject_sql):
        test_session = self.session
        course_sql = CourseSQL(
            subject_id=subject_sql.id,
            start_date=datetime.strptime('2024-03-16', '%Y-%m-%d').date(),
            end_date=datetime.strptime('2024-06-16', '%Y-%m-%d').date(),
            professor='Bill Gates',
            classroom='404',
        )
        test_session.add(course_sql)
        test_session.commit()
        test_session.refresh(course_sql)
        return course_sql

    def _generate_lead(self, id: str = ''):
        test_session = self.session
        address_sql = AddressSQL(
            street='Av. Colon',
            number=100,
            city='Cordoba',
            province='Cordoba',
            country='Argentina',
        )
        lead_sql = LeadSQL(
            first_name='Charly',
            last_name='Garcia',
            email=f"charly.snm{id}@gmail.com",
            phone_number="3515555555",
            career_id=1,
            address=address_sql,
            year_of_inscription=2021,
        )
        test_session.add(lead_sql)
        test_session.commit()

    def _generate_enrollment(self):
        test_session = self.session
        enrollment = Enrollment(
            lead_id=1,
            course_id=1,
            subject_times_taken=1,
        )
        enrollment_sql = EnrollmentPersistanceAdapter.domain_to_persistance(enrollment)
        test_session.add(enrollment_sql)
        test_session.commit()

    def _generate_support_objects(self):
        subjects_sql = self._generate_subjects()
        self._generate_career(subjects_sql)
        self._generate_course(subjects_sql[0])

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, test_session: Session):
        self.session: Session = test_session


from glob import glob

def refactor(string: str) -> str:
    return string.replace("/", ".").replace("\\", ".").replace(".py", "")

pytest_plugins = [
    refactor(fixture) for fixture in glob("test/fixtures/*.py") if "__" not in fixture
]
