"""Configurazione e fixtures per i test.

Usa SQLite in-memory con engine globale condiviso.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.database import Base, get_db
from app.main import create_app

# Engine condiviso: StaticPool mantiene un unico DB in-memory per tutte le sessioni
TEST_ENGINE = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=TEST_ENGINE)


@pytest.fixture(scope="function")
def test_db():
    """Crea le tabelle in SQLite in-memory e restituisce una sessione.

    Ogni test parte con database pulito.
    """
    Base.metadata.create_all(bind=TEST_ENGINE)
    session = TestSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=TEST_ENGINE)


@pytest.fixture(scope="function")
def client(test_db):
    """Restituisce un TestClient con override della dipendenza del DB."""
    app = create_app(test_mode=True)

    def _override_get_db():
        yield test_db

    app.dependency_overrides[get_db] = _override_get_db
    with TestClient(app) as c:
        yield c
