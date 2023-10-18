from typing import Any

from fastapi import APIRouter, status, Depends
from domain.exceptions import LeadAlreadyExists
from api.v1.exceptions import (
    LeadDoesNotExist,
    LeadAlreadyExists as LeadAlreadyExistsApiException,
)
from api.v1.adapters.lead_adapter import LeadClientAdapter
from api.v1.dtos.lead import LeadCreate, LeadRead
from api.v1.dependencies.domain_services import get_lead_service
from domain.services.lead_service import LeadService


router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[LeadRead],
)
def get_leads(
    email: str | None = None,
    lead_service: LeadService = Depends(get_lead_service),
):
    filters = {}
    if email:
        filters["email"] = email

    domain_leads = lead_service.get_leads(filters=filters)
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
    if not domain_lead:
        raise LeadDoesNotExist

    client_lead = LeadClientAdapter.domain_to_client(domain_lead)
    return client_lead


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create_lead(
    lead: LeadCreate,
    lead_service: LeadService = Depends(get_lead_service),
):
    domain_lead = LeadClientAdapter.client_to_domain(lead)
    try:
        created_lead = lead_service.create_lead(lead=domain_lead)
    except LeadAlreadyExists:
        raise LeadAlreadyExistsApiException
    return created_lead.id
