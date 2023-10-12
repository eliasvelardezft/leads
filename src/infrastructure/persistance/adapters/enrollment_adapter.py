from domain.interfaces.adapters import IPersistanceAdapter
from domain.models.enrollment import Enrollment
from domain.models.value_objects import Name
from infrastructure.persistance.models import EnrollmentSQL
from .lead_adapter import LeadPersistanceAdapter
from .course_adapter import CoursePersistanceAdapter
from .status_change_adapter import StatusChangePersistanceAdapter


class EnrollmentPersistanceAdapter(IPersistanceAdapter):
    @staticmethod
    def domain_to_persistance(enrollment: Enrollment) -> EnrollmentSQL:
        persistance_status_changes = [
            StatusChangePersistanceAdapter.domain_to_persistance(status_change)
            for status_change in enrollment.status_changes
        ]
        return EnrollmentSQL(
            lead_id=enrollment.lead_id,
            course_id=enrollment.course_id,
            subject_times_taken=enrollment.subject_times_taken,
            status_changes=persistance_status_changes,
        )

    @staticmethod
    def persistance_to_domain(enrollment: EnrollmentSQL) -> Enrollment:
        domain_lead = LeadPersistanceAdapter.persistance_to_domain(enrollment.lead)
        domain_course = CoursePersistanceAdapter.persistance_to_domain(enrollment.course)
        domain_status_changes = [
            StatusChangePersistanceAdapter.persistance_to_domain(status_change)
            for status_change in enrollment.status_changes
        ]
        return Enrollment(
            id=enrollment.id,
            lead=domain_lead,
            lead_id=enrollment.lead_id,
            course=domain_course,
            course_id=enrollment.course_id,
            subject_times_taken=enrollment.subject_times_taken,
            status_changes=domain_status_changes,
        )
