from api.v1.dtos import CourseCreate, CourseRead
from api.v1.adapters.subject_adapter import SubjectClientAdapter
from domain.models import Course
from domain.interfaces.adapters import IClientAdapter



class CourseClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(course: CourseCreate) -> Course:
        return Course(
            subject_id=course.subject_id,
            start_date=course.start_date,
            end_date=course.end_date,
            professor=course.professor,
            classroom=course.classroom,
        )

    @staticmethod
    def domain_to_client(course: Course) -> CourseRead:
        client_subject = SubjectClientAdapter.domain_to_client(subject=course.subject)
        return CourseRead(
            id=course.id,
            subject=client_subject,
            subject_id=course.subject.id,
            start_date=course.start_date,
            end_date=course.end_date,
            professor=course.professor,
            classroom=course.classroom,
        )
