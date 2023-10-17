import pytest
from typing import Generator
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from main import app
from infrastructure.persistance.base import Base
from sqlalchemy.engine.base import Engine
from domain.services import LeadService, EnrollmentService
from api.v1.dependencies.domain_services import (
    get_admin_service,
    get_enrollment_service,
    get_lead_service, 
)


@pytest.fixture(scope="session")
def db_engine() -> Generator[Engine, None, None]:
    engine = create_engine("sqlite:///:memory:?check_same_thread=False")
    Base.metadata.create_all(engine)
    yield engine


@pytest.fixture(scope="function")
def test_session(db_engine) -> Generator[Session, None, None]:
    connection = db_engine.connect()
    connection.begin()

    session = Session(bind=connection)

    yield session

    session.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(test_session: Session) -> Generator[TestClient, None, None]:
    app.dependency_overrides[get_lead_service] = lambda: get_lead_service(test_session)
    app.dependency_overrides[get_enrollment_service] = lambda: get_enrollment_service(test_session)
    app.dependency_overrides[get_admin_service] = lambda: get_admin_service(test_session)

    with TestClient(app) as c:
        yield c
