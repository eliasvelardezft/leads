from sqlalchemy.orm import Session
from domain.interfaces import IRepository
from domain.models import Course
from infrastructure.persistance.base import engine
from infrastructure.persistance.adapters import CoursePersistanceAdapter
from infrastructure.persistance.models import CourseSQL


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

    def create(self, course: Course) -> Course:
        import ipdb; ipdb.set_trace()
        db_course = CoursePersistanceAdapter.domain_to_persistance(course)
        self.session.add(db_course)
        self.session.commit()
        self.session.refresh(db_course)
        course = CoursePersistanceAdapter.persistance_to_domain(db_course)
        return course
