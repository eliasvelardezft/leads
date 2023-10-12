from fastapi import APIRouter

from .lead import router as leads_router
from .admin import router as admin_router
from .enrollment import router as enrollment_router


router = APIRouter()


router.include_router(leads_router, prefix="/leads", tags=["leads"])
router.include_router(admin_router, prefix="/admin", tags=["admin"])
router.include_router(enrollment_router, prefix="/enrollments", tags=["enrollments"])
