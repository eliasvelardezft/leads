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


def get_admin_service() -> AdminService:
    return AdminService(
        career_repository=CareerRepository(),
        subject_repository=SubjectRepository(),
        course_repository=CourseRepository(),
    )


def get_lead_service() -> LeadService:
    return LeadService(repository=LeadRepository())


def get_enrollment_service() -> EnrollmentService:
    return EnrollmentService(
        repository=EnrollmentRepository(),
        status_change_repository=StatusChangeRepository(),
    )
