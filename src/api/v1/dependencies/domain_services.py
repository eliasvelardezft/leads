from sqlalchemy.orm import Session
from fastapi import Depends

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
from infrastructure.paginator import Paginator
from infrastructure.persistance.base import get_session


def get_admin_service(session: Session = Depends(get_session)) -> AdminService:
    return AdminService(
        career_repository=CareerRepository(session),
        subject_repository=SubjectRepository(session),
        course_repository=CourseRepository(session),
    )


def get_lead_service(session: Session = Depends(get_session)) -> LeadService:
    return LeadService(
        repository=LeadRepository(session),
        paginator=Paginator,
    )


def get_enrollment_service(session: Session = Depends(get_session)) -> EnrollmentService:
    return EnrollmentService(
        repository=EnrollmentRepository(session),
        status_change_repository=StatusChangeRepository(session),
    )
