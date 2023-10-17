from domain.models.enrollment import Enrollment
from domain.models.status import (
    EnrollmentStatus,
    CreatedStatus,
    StatusChangeAction,
    StatusChange
)


def test_enrollment_creation():
    enrollment = Enrollment(
        subject_times_taken=1,
        lead_id=1,
        course_id=1,
    )
    assert enrollment.subject_times_taken == 1
    assert len(enrollment.status_changes) == 1
    assert isinstance(enrollment.status_changes[0].status, CreatedStatus)
    assert enrollment.status_changes[0].status.status == EnrollmentStatus.CREATED


def test_enrollment_progress(domain_enrollment):
    domain_enrollment.progress()

    current_status = domain_enrollment.get_current_status()

    assert len(domain_enrollment.status_changes) == 2
    assert isinstance(current_status.status, EnrollmentStatus)
    assert current_status.status == EnrollmentStatus.PROGRESS


def test_enrollment_complete(domain_enrollment):
    domain_enrollment.progress()
    domain_enrollment.complete()

    current_status = domain_enrollment.get_current_status()

    assert len(domain_enrollment.status_changes) == 3
    assert isinstance(current_status.status, EnrollmentStatus)
    assert current_status.status == EnrollmentStatus.COMPLETED


def test_enrollment_fail(domain_enrollment):
    domain_enrollment.progress()
    domain_enrollment.fail()

    current_status = domain_enrollment.get_current_status()

    assert len(domain_enrollment.status_changes) == 3
    assert isinstance(current_status.status, EnrollmentStatus)
    assert current_status.status == EnrollmentStatus.FAILED


def test_enrollment_drop(domain_enrollment):
    domain_enrollment.progress()
    domain_enrollment.drop()

    current_status = domain_enrollment.get_current_status()

    assert len(domain_enrollment.status_changes) == 3
    assert isinstance(current_status.status, EnrollmentStatus)
    assert current_status.status == EnrollmentStatus.DROPPED


def test_enrollment_lifecycle():
    enrollment = Enrollment(
        subject_times_taken=1,
        lead_id=1,
        course_id=1,
    )

    # created can only call progress or drop
    try:
        enrollment.complete()
        assert False
    except NotImplementedError:
        assert True
    try:
        enrollment.fail()
        assert False
    except NotImplementedError:
        assert True

    enrollment.progress()
    # progress can NOT call progress

    try:
        enrollment.progress()
        assert False
    except NotImplementedError:
        assert True

    enrollment.complete()
    # complete cant change status

    try:
        enrollment.complete()
        assert False
    except NotImplementedError:
        assert True
    try:
        enrollment.fail()
        assert False
    except NotImplementedError:
        assert True
    try:
        enrollment.drop()
        assert False
    except NotImplementedError:
        assert True
    try:
        enrollment.progress()
        assert False
    except NotImplementedError:
        assert True
