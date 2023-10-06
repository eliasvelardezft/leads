from dataclasses import dataclass


@dataclass
class LeadSQL:
    id: str
    first_name: str
    last_name: str
    email: str
