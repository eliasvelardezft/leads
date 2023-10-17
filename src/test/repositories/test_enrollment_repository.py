from domain.models import Enrollment
from test.conftest import BaseTestClass
from infrastructure.persistance.repositories import EnrollmentRepository

class TestEnrollmentRepository(BaseTestClass):
    def test_create(self, test_enrollment_repository: EnrollmentRepository):
        self._generate_support_objects()
        self._generate_lead()

        enrollment = Enrollment(
            subject_times_taken=1,
            lead_id=1,
            course_id=1,
        )
        test_enrollment_repository.create(enrollment)

        enrollment = test_enrollment_repository.get(1)
        assert enrollment.subject_times_taken == 1
        assert len(enrollment.status_changes) == 1

    def test_filter(self, test_enrollment_repository: EnrollmentRepository):
        self._generate_support_objects()
        self._generate_lead()

        enrollment1 = Enrollment(
            subject_times_taken=1,
            lead_id=1,
            course_id=1,
        )
        enrollment2 = Enrollment(
            subject_times_taken=2,
            lead_id=1,
            course_id=1,
        )
        test_enrollment_repository.create(enrollment1)
        test_enrollment_repository.create(enrollment2)

        enrollments = test_enrollment_repository.filter(
            filters={
                "subject_times_taken": 2
            }
        )
        assert len(enrollments) == 1
        assert enrollments[0].id == 2
        assert enrollments[0].subject_times_taken == 2

    def test_get(self, test_enrollment_repository: EnrollmentRepository):
        self._generate_support_objects()
        self._generate_lead()

        enrollment = Enrollment(
            subject_times_taken=1,
            lead_id=1,
            course_id=1,
        )
        test_enrollment_repository.create(enrollment)

        enrollment = test_enrollment_repository.get(1)

        assert enrollment is not None
        assert enrollment.id == 1
        assert enrollment.subject_times_taken == 1

    def test_bulk_create(self, test_enrollment_repository: EnrollmentRepository):
        self._generate_support_objects()
        self._generate_lead()

        enrollment1 = Enrollment(
            subject_times_taken=1,
            lead_id=1,
            course_id=1,
        )
        enrollment2 = Enrollment(
            subject_times_taken=2,
            lead_id=1,
            course_id=1,
        )
        test_enrollment_repository.bulk_create([enrollment1, enrollment2])

        enrollments = test_enrollment_repository.filter()

        assert len(enrollments) == 2
        assert enrollments[0].id == 1
        assert enrollments[0].subject_times_taken == 1
        assert enrollments[1].id == 2
        assert enrollments[1].subject_times_taken == 2