from domain.models import Career

from domain.interfaces.repository import IRepository


class AdminService:
    def __init__(
        self,
        career_repository: IRepository,
    ):
        self.career_repository = career_repository

    def create_career(self, career: Career) -> Career:
        return self.career_repository.create(career)

    def get_career(self, id: str) -> Career:
        return self.career_repository.get(id)

    def get_all_careers(self) -> list[Career]:
        return self.career_repository.get_all()
