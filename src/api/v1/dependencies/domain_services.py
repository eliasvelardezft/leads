from domain.services import (
    AdminService,
    LeadService,
    EnrollmentService,
)
from infrastructure.persistance.repositories import (
    CareerRepository,
    SubjectRepository,
    CourseRepository,
    LeadRepository,
    EnrollmentRepository,
    StatusChangeRepository,
)


def get_admin_service(session = None) -> AdminService:
    return AdminService(
        career_repository=CareerRepository(session),
        subject_repository=SubjectRepository(session),
        course_repository=CourseRepository(session),
    )


def get_lead_service(session = None) -> LeadService:
    return LeadService(repository=LeadRepository(session))


def get_enrollment_service(session = None) -> EnrollmentService:
    return EnrollmentService(
        repository=EnrollmentRepository(session),
        status_change_repository=StatusChangeRepository(session),
    )
