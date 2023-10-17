from domain.interfaces.adapters import IPersistanceAdapter
from domain.models.course import Course
from domain.models.value_objects import Name
from infrastructure.persistance.models import CourseSQL
from infrastructure.persistance.adapters import SubjectPersistanceAdapter


class CoursePersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(course: Course) -> CourseSQL:
        return CourseSQL(
            id=course.id,
            start_date=course.start_date,
            end_date=course.end_date,
            professor=course.professor,
            classroom=course.classroom,
            subject_id=course.subject_id,
        )
    
    @staticmethod
    def persistance_to_domain(course: CourseSQL) -> Course:
        domain_subject = SubjectPersistanceAdapter.persistance_to_domain(course.subject)
        return Course(
            id=course.id,
            start_date=course.start_date,
            end_date=course.end_date,
            professor=course.professor,
            classroom=course.classroom,
            subject=domain_subject,
            subject_id=course.subject_id,
        )
