from fastapi import APIRouter, status, Depends, Response

from api.v1.adapters.lead_adapter import LeadClientAdapter
from api.v1.dtos.lead import LeadCreate, LeadRead
from api.v1.dependencies import get_lead_service
from domain.services.lead_service import LeadService

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[LeadRead],
)
def get_leads(
    lead_service: LeadService = Depends(get_lead_service),
):
    domain_leads = lead_service.get_all_leads()
    client_leads = [
        LeadClientAdapter.domain_to_client(lead)
        for lead in domain_leads
    ]
    return client_leads


@router.get(
    "/{lead_id}",
    status_code=status.HTTP_200_OK,
    response_model=LeadRead,
)
def get_lead(
    lead_id: int,
    lead_service: LeadService = Depends(get_lead_service),
):
    domain_lead = lead_service.get_lead(id=lead_id)
    client_lead = LeadClientAdapter.domain_to_client(domain_lead)
    return client_lead


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create_lead(
    lead: LeadCreate,
    response: Response,
    lead_service: LeadService = Depends(get_lead_service),
):
    domain_lead = LeadClientAdapter.client_to_domain(lead)
    created_lead = lead_service.register_lead(lead=domain_lead)
    response.headers["Location"] = f"/leads/{created_lead.id}"
    return

