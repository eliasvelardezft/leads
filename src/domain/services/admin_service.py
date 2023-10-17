from typing import Any

from domain.models import Career, Subject, Course

from domain.interfaces.repository import IRepository


class AdminService:
    def __init__(
        self,
        career_repository: IRepository,
        subject_repository: IRepository,
        course_repository: IRepository
    ):
        self.career_repository = career_repository
        self.subject_repository = subject_repository
        self.course_repository = course_repository


    # careers
    def create_career(self, career: Career) -> Career:
        return self.career_repository.create(career)

    def get_career(self, id: str) -> Career:
        return self.career_repository.get(id)

    def get_careers(self, filters: dict[str, Any]) -> list[Career]:
        return self.career_repository.filter(filters)

    # subjects
    def create_subject(self, subject: Subject) -> Subject:
        return self.subject_repository.create(subject)

    def get_subject(self, id: str) -> Subject:
        return self.subject_repository.get(id)

    def get_subjects(self, filters: dict[str, Any]) -> list[Subject]:
        return self.subject_repository.filter(filters)

    # courses
    def create_course(self, course: Course) -> Course:
        return self.course_repository.create(course)

    def get_course(self, id: str) -> Course:
        return self.course_repository.get(id)

    def get_courses(self, filters: dict[str, Any]) -> list[Course]:
        return self.course_repository.filter(filters)
