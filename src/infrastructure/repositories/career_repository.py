from domain.interfaces import IRepository

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

    def get(self, id: str):
        return filter(lambda career: career["id"] == id, self.careers)

    def get_all(self):
        return self.careers

    def create(self, career):
        career.id = len(self.careers) + 1
        self.careers.append(career)
        return career
