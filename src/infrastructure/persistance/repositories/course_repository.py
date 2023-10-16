from typing import Any

from sqlalchemy.orm import Session

from domain.interfaces import IRepository
from domain.exceptions import InvalidFilter
from domain.models import Course
from infrastructure.persistance.base import engine
from infrastructure.persistance.adapters import CoursePersistanceAdapter
from infrastructure.persistance.models import CourseSQL, SubjectSQL


class CourseRepository(IRepository):
    def __init__(self, session: Session | None = None) -> None:
        if session:
            self.session = session
        else:
            self.session = Session(engine)

    def get(self, id: str) -> Course | None:
        db_course = self.session.query(CourseSQL).filter(CourseSQL.id == id).first()
        course = None
        if db_course:
            course = CoursePersistanceAdapter.persistance_to_domain(db_course)
        return course

    def get_all(self) -> list[Course]:
        db_courses = self.session.query(CourseSQL).all()
        courses = [CoursePersistanceAdapter.persistance_to_domain(course) for course in db_courses]
        return courses

    def filter(self, filters: dict[str, Any]) -> list[Course]:
        query = self.session.query(CourseSQL)
        for key, value in filters.items():
            try:
                if key == "subject_id":
                    query = query.join(
                        SubjectSQL
                    ).filter(SubjectSQL.id == value)
                else:
                    query = query.filter(getattr(CourseSQL, key) == value)
            except Exception as e:
                raise InvalidFilter(f"Invalid filter: {key}={value}")
        db_courses = query.all()
        courses = [
            CoursePersistanceAdapter.persistance_to_domain(Course)
            for Course in db_courses
        ]
        return courses

    def create(self, course: Course) -> Course:
        db_course = CoursePersistanceAdapter.domain_to_persistance(course)
        self.session.add(db_course)
        self.session.commit()
        self.session.refresh(db_course)
        course = CoursePersistanceAdapter.persistance_to_domain(db_course)
        return course
