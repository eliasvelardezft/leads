from typing import Any

from fastapi import APIRouter, status, Depends, Response, Request

from api.v1.adapters import (
    CareerClientAdapter,
    SubjectClientAdapter,
    CourseClientAdapter
)
from api.v1.dtos import (
    CareerCreate,
    CareerRead,
    SubjectCreate,
    SubjectRead,
    CourseCreate,
    CourseRead,
)
from api.v1.dependencies.domain_services import get_admin_service
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


@router.get(
    "/career",
    response_model=list[CareerRead],
    status_code=status.HTTP_200_OK,
)
def get_careers(
    admin_service: AdminService = Depends(get_admin_service),
):
    careers = admin_service.get_all_careers()
    client_careers = [
        CareerClientAdapter.domain_to_client(career=career)
        for career in careers
    ]
    return client_careers


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


@router.get(
    "/subject/{subject_id}",
    response_model=SubjectRead,
    status_code=status.HTTP_200_OK,
)
def get_subject(
    subject_id: int,
    admin_service: AdminService = Depends(get_admin_service),
):
    subject = admin_service.get_subject(id=subject_id)
    client_subject = SubjectClientAdapter.domain_to_client(subject=subject)
    return client_subject


@router.get(
    "/subject",
    response_model=list[SubjectRead],
    status_code=status.HTTP_200_OK,
)
def get_subjects(
    request: Request,
    career_id: int = None,
    admin_service: AdminService = Depends(get_admin_service),
):
    filters = {}
    if career_id:
        filters["career_id"] = career_id

    subjects = admin_service.filter_subjects(filters)
    client_subjects = [
        SubjectClientAdapter.domain_to_client(subject=subject)
        for subject in subjects
    ]
    return client_subjects


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


@router.get(
    "/course/{course_id}",
    response_model=CourseRead,
    status_code=status.HTTP_200_OK,
)
def get_course(
    course_id: int,
    admin_service: AdminService = Depends(get_admin_service),
):
    course = admin_service.get_course(id=course_id)
    client_course = CourseClientAdapter.domain_to_client(course=course)
    return client_course


@router.get(
    "/course",
    response_model=list[CourseRead],
    status_code=status.HTTP_200_OK,
)
def get_courses(
    subject_id: int | None = None,
    admin_service: AdminService = Depends(get_admin_service),
):
    filters = {}
    if subject_id:
        filters["subject_id"] = subject_id

    courses = admin_service.filter_courses(filters=filters)
    client_courses = [
        CourseClientAdapter.domain_to_client(course=course)
        for course in courses
    ]
    return client_courses
