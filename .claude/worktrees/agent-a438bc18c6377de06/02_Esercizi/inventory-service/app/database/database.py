"""Gestione della connessione al database con SQLAlchemy.

Supporta due modalità:
  - SQLite  (default, per sviluppo/test in-memory)
  - PostgreSQL (produzione, container separato)
"""
import logging
import os

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    """Classe base dichiarativa per tutti i modelli SQLAlchemy."""
    pass


# Crea la directory per SQLite se necessario
if settings.DATABASE_TYPE != "postgres":
    db_dir = os.path.dirname(settings.DATABASE_PATH)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)
    logger.info("Using SQLite database at %s", settings.DATABASE_PATH)
else:
    logger.info("Using PostgreSQL database at %s", settings.DATABASE_HOST)

engine = create_engine(
    settings.sqlalchemy_url,
    echo=False,
    connect_args={"check_same_thread": False} if settings.DATABASE_TYPE != "postgres" else {},
)

# Log SQL statements in DEBUG mode (set via LOG_LEVEL env var)
if os.environ.get("LOG_LEVEL", "").upper() == "DEBUG":

    @event.listens_for(Engine, "before_cursor_execute")
    def before_cursor_execute(  # noqa: ANN202
        conn, cursor, statement, parameters, context, executemany  # noqa: ANN001
    ):
        logger.debug("SQL: %s", statement.replace("\n", " ").strip())
        if parameters:
            logger.debug("Params: %s", parameters)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_database():
    """Crea tutte le tabelle definite nei modelli SQLAlchemy."""
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")


def get_db():
    """Dipendenza FastAPI per ottenere una sessione SQLAlchemy."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
