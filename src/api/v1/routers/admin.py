from fastapi import APIRouter, status, Depends, Response

from api.v1.adapters import (
    CareerClientAdapter,
    SubjectClientAdapter,
    CourseClientAdapter
)
from api.v1.dtos import (
    CareerCreate,
    CareerRead,
    SubjectCreate,
    CourseCreate,
)
from api.v1.dependencies import get_admin_service
from domain.services.admin_service import AdminService


router = APIRouter()


@router.post(
    "/career",
    status_code=status.HTTP_201_CREATED,
)
def create_career(
    career: CareerCreate,
    response: Response,
    admin_service: AdminService = Depends(get_admin_service),
):
    domain_career = CareerClientAdapter.client_to_domain(career)
    created_career = admin_service.create_career(career=domain_career)
    response.headers["Location"] = f"/admin/career/{created_career.id}"
    return


@router.get(
    "/career/{career_id}",
    response_model=CareerRead,
    status_code=status.HTTP_200_OK,
)
def get_career(
    career_id: int,
    admin_service: AdminService = Depends(get_admin_service),
):
    career = admin_service.get_career(id=career_id)
    client_career = CareerClientAdapter.domain_to_client(career=career)
    return client_career


@router.post(
    "/subject",
    status_code=status.HTTP_201_CREATED,
)
def create_subject(
    subject: SubjectCreate,
    response: Response,
    admin_service: AdminService = Depends(get_admin_service),
):
    domain_subject = SubjectClientAdapter.client_to_domain(subject)
    created_subject = admin_service.create_subject(subject=domain_subject)
    response.headers["Location"] = f"/admin/subject/{created_subject.id}"
    return


@router.post(
    "/course",
    status_code=status.HTTP_201_CREATED,
)
def create_course(
    course: CourseCreate,
    response: Response,
    admin_service: AdminService = Depends(get_admin_service),
):
    domain_course = CourseClientAdapter.client_to_domain(course)
    created_course = admin_service.create_course(course=domain_course)
    response.headers["Location"] = f"/admin/course/{created_course.id}"
    return
