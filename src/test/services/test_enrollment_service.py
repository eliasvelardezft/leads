from dataclasses import replace

from domain.services import EnrollmentService
from domain.models.status import (
    CreatedStatus,
    EnrollmentStatus,
)
from test.conftest import BaseTestClass


class TestEnrollmentService(BaseTestClass):
    def test_create_enrollment(
        self,
        domain_enrollment,
        test_enrollment_service: EnrollmentService
    ):
        self._generate_support_objects()
        self._generate_lead()

        enrollment = test_enrollment_service.create_enrollment(
            domain_enrollment
        )
        current_status = enrollment.get_current_status()
        assert enrollment.subject_times_taken == 1
        assert len(enrollment.status_changes) == 1
        assert isinstance(current_status, CreatedStatus)
        assert current_status.status == EnrollmentStatus.CREATED

    def test_create_enrollments(
        self,
        domain_enrollment,
        test_enrollment_service: EnrollmentService
    ):
        self._generate_support_objects()
        self._generate_lead()
        self._generate_lead(id="2")

        enrollment1 = domain_enrollment

        enrollment2 = replace(domain_enrollment)
        enrollment2.subject_times_taken = 2
        enrollment2.lead_id = 2

        enrollments = test_enrollment_service.create_enrollments(
            [enrollment1, enrollment2]
        )
        assert len(enrollments) == 2
        assert enrollments[0].subject_times_taken == 1
        assert len(enrollments[0].status_changes) == 1
        assert isinstance(enrollments[0].get_current_status(), CreatedStatus)
        assert enrollments[0].get_current_status().status == EnrollmentStatus.CREATED
        assert enrollments[1].subject_times_taken == 2
        assert len(enrollments[1].status_changes) == 1
        assert isinstance(enrollments[1].get_current_status(), CreatedStatus)
        assert enrollments[1].get_current_status().status == EnrollmentStatus.CREATED

    def test_filter_enrollments(
        self,
        domain_enrollment,
        test_enrollment_service: EnrollmentService
    ):
        self._generate_support_objects()
        self._generate_lead()
        self._generate_lead(id="2")

        enrollment1 = domain_enrollment

        enrollment2 = replace(domain_enrollment)
        enrollment2.subject_times_taken = 2
        enrollment2.lead_id = 2

        test_enrollment_service.create_enrollments(
            [enrollment1, enrollment2]
        )

        enrollments = test_enrollment_service.get_enrollments(
            filters={
                'subject_times_taken': 1,
            }
        )
        assert len(enrollments) == 1
        assert enrollments[0].subject_times_taken == 1

    def test_filter_by_lead(
        self,
        domain_enrollment,
        test_enrollment_service: EnrollmentService
    ):
        self._generate_support_objects()
        self._generate_lead()

        self._generate_lead(id="2")

        enrollment1 = domain_enrollment

        enrollment2 = replace(domain_enrollment)
        enrollment2.lead_id = 2
        enrollment2.subject_times_taken = 2

        test_enrollment_service.create_enrollments(
            [enrollment1, enrollment2]
        )

        enrollments = test_enrollment_service.get_enrollments(
            filters={
                'lead': {
                    'email': "charly.snm2@gmail.com",
                }
            }
        )
        assert len(enrollments) == 1
        assert enrollments[0].subject_times_taken == 2

    def test_get_enrollment(
        self,
        domain_enrollment,
        test_enrollment_service: EnrollmentService
    ):
        self._generate_support_objects()
        self._generate_lead()

        enrollment = test_enrollment_service.get_enrollment(id="1")
        assert enrollment is None

        test_enrollment_service.create_enrollment(
            domain_enrollment
        )

        enrollment = test_enrollment_service.get_enrollment(id="1")
        current_status = enrollment.get_current_status()
        assert enrollment.subject_times_taken == 1
        assert len(enrollment.status_changes) == 1
        assert isinstance(current_status, CreatedStatus)
        assert current_status.status == EnrollmentStatus.CREATED

    def test_get_all_enrollments(
        self,
        domain_enrollment,
        test_enrollment_service: EnrollmentService
    ):
        self._generate_support_objects()
        self._generate_lead()
        self._generate_lead(id="2")

        enrollment1 = domain_enrollment

        enrollment2 = replace(domain_enrollment)
        enrollment2.subject_times_taken = 2
        enrollment2.lead_id = 2

        test_enrollment_service.create_enrollments(
            [enrollment1, enrollment2]
        )

        enrollments = test_enrollment_service.get_enrollments()
        assert len(enrollments) == 2
        assert enrollments[0].subject_times_taken == 1
        assert len(enrollments[0].status_changes) == 1
        assert isinstance(enrollments[0].get_current_status(), CreatedStatus)
        assert enrollments[0].get_current_status().status == EnrollmentStatus.CREATED
        assert enrollments[1].subject_times_taken == 2
        assert len(enrollments[1].status_changes) == 1
        assert isinstance(enrollments[1].get_current_status(), CreatedStatus)
        assert enrollments[1].get_current_status().status == EnrollmentStatus.CREATED
