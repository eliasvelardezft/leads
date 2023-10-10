from domain.services.admin_service import AdminService
from infrastructure.persistance.repositories import CareerRepository, SubjectRepository


def get_admin_service() -> AdminService:
    return AdminService(
        career_repository=CareerRepository(),
        subject_repository=SubjectRepository(),
    )
