from fastapi import APIRouter

from .lead import router as leads_router


router = APIRouter()


router.include_router(leads_router, prefix="/leads", tags=["leads"])
