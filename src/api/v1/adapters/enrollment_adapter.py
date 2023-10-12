from api.v1.dtos.enrollment import EnrollmentCreate, EnrollmentRead
from domain.interfaces import IClientAdapter
from domain.models import Enrollment
from api.v1.adapters.lead_adapter import LeadClientAdapter
from api.v1.adapters.course_adapter import CourseClientAdapter
from api.v1.adapters.status_change_adapter import StatusChangeClientAdapter


class EnrollmentClientAdapter(IClientAdapter):
    @staticmethod
    def client_to_domain(enrollment: EnrollmentCreate) -> Enrollment:
        return Enrollment(
            lead_id=enrollment.lead_id,
            course_id=enrollment.course_id,
            subject_times_taken=enrollment.subject_times_taken,
        )

    @staticmethod
    def domain_to_client(enrollment: Enrollment) -> EnrollmentRead:
        client_lead = LeadClientAdapter.domain_to_client(enrollment.lead)
        client_course = CourseClientAdapter.domain_to_client(enrollment.course)
        client_status_changes = [
            StatusChangeClientAdapter.domain_to_client(status_change)
            for status_change in enrollment.status_changes
        ]
        return EnrollmentRead(
            id=enrollment.id,
            lead_id=enrollment.lead_id,
            lead=client_lead,
            course_id=enrollment.course_id,
            course=client_course,
            subject_times_taken=enrollment.subject_times_taken,
            status_changes=client_status_changes
        )
