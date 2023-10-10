from domain.interfaces import IRepository
from infrastructure.persistance.adapters import CareerPersistanceAdapter
from domain.models import Career
# TODO: implement real repository with sqlalchemy
from collections import namedtuple
FakeCareer = namedtuple("Career", ["id", "name", "description"])


class CareerRepository(IRepository):
    careers = [
        FakeCareer(
            id=1,
            name="Ingenieria en Sistemas",
            description="Ingenieria en sistemas es una carrera que se enfoca en la programacion",
        ),
        FakeCareer(
            id=2,
            name="Ingenieria en Electronica",
            description="Ingenieria en electronica es una carrera que se enfoca en la electronica",
        )
    ]

    def get(self, id: str) -> Career:
        db_career = filter(lambda career: career.id == id, self.careers)
        db_career = list(db_career)[0]
        career = CareerPersistanceAdapter.persistance_to_domain(db_career)
        return career

    def get_all(self) -> list[Career]:
        all_db_careers = self.careers
        all_careers = [
            CareerPersistanceAdapter.persistance_to_domain(career)
            for career in all_db_careers
        ]
        return all_careers

    def create(self, career: Career) -> Career:
        db_career = career
        db_career.id = len(self.careers) + 1
        self.careers.append(db_career)
        career = CareerPersistanceAdapter.persistance_to_domain(db_career)
        return career
