from pydantic import BaseModel

from .career import CareerRead
from .status import StatusChangeRead


class EnrollmentBase(BaseModel):
    subject_times_taken: int
    lead_id: int
    course_id: int


class EnrollmentCreate(EnrollmentBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "subject_times_taken": 1,
                    "lead_id": "1",
                    "course_id": "1",
                }
            ]
        }
    }


class EnrollmentRead(EnrollmentBase):
    id: int
    status_changes: list[StatusChangeRead]

    class Config:
        from_attributes = True


class LeadUpdate(EnrollmentBase):
    subject_times_taken: int | None = None
    lead_id: int | None = None
    course_id: int | None = None
