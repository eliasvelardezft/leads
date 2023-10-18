from typing import Any

from fastapi import APIRouter, status, Depends, Response

from api.v1.exceptions import EntityDoesNotExist, EntityAlreadyExists
from api.v1.adapters.enrollment_adapter import EnrollmentClientAdapter
from api.v1.dtos.enrollment import EnrollmentCreate, EnrollmentRead
from api.v1.dependencies.domain_services import get_enrollment_service
from domain.services.enrollment_service import EnrollmentService
from domain.exceptions import EnrollmentAlreadyExists

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[EnrollmentRead],
)
def get_enrollments(
    lead_email: str | None = None,
    lead_id: int | None = None,
    enrollment_service: EnrollmentService = Depends(get_enrollment_service),
):
    filters = {}
    if lead_email:
        filters = {
            "lead": {
                "email": lead_email,
            }
        }
    elif lead_id:
        filters["lead_id"] = lead_id

    enrollments = enrollment_service.get_enrollments(filters=filters)
    client_enrollments = [
        EnrollmentClientAdapter.domain_to_client(enrollment)
        for enrollment in enrollments
    ]
    return client_enrollments


@router.get(
    "/{enrollment_id}",
    status_code=status.HTTP_200_OK,
    response_model=EnrollmentRead,
)
def get_enrollment(
    enrollment_id: int,
    enrollment_service: EnrollmentService = Depends(get_enrollment_service),
):
    enrollment = enrollment_service.get_enrollment(id=enrollment_id)
    if not enrollment:
        raise EntityDoesNotExist
    client_enrollment = EnrollmentClientAdapter.domain_to_client(enrollment)
    return client_enrollment


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create_enrollment(
    enrollment: EnrollmentCreate,
    response: Response,
    enrollment_service: EnrollmentService = Depends(get_enrollment_service),
):
    enrollment = EnrollmentClientAdapter.client_to_domain(enrollment)
    try:
        created_enrollment = enrollment_service.create_enrollment(enrollment=enrollment)
    except EnrollmentAlreadyExists:
        raise EntityAlreadyExists
    client_enrollment = EnrollmentClientAdapter.domain_to_client(created_enrollment)
    return client_enrollment


@router.post(
    "/bulk",
    status_code=status.HTTP_201_CREATED,
)
def create_enrollments(
    enrollments: list[EnrollmentCreate],
    response: Response,
    enrollment_service: EnrollmentService = Depends(get_enrollment_service),
):
    domain_enrollments = [
        EnrollmentClientAdapter.client_to_domain(enrollment)
        for enrollment in enrollments
    ]
    try:
        created_enrollments = enrollment_service.create_enrollments(enrollments=domain_enrollments)
    except EnrollmentAlreadyExists:
        raise EntityAlreadyExists
    client_enrollments = [
        EnrollmentClientAdapter.domain_to_client(enrollment)
        for enrollment in created_enrollments
    ]
    return client_enrollments
