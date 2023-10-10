from fastapi import APIRouter, status, Depends, Response

from api.v1.adapters.career_adapter import CareerClientAdapter
from api.v1.dtos.career import CareerCreate, CareerRead
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
