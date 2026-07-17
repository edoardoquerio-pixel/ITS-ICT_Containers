"""Gestione della connessione al database con SQLAlchemy."""
import logging
import os

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    pass


if settings.DATABASE_TYPE != "postgres":
    db_dir = os.path.dirname(settings.DATABASE_PATH)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

engine = create_engine(
    settings.sqlalchemy_url,
    echo=False,
    connect_args={"check_same_thread": False} if settings.DATABASE_TYPE != "postgres" else {},
)

if os.environ.get("LOG_LEVEL", "").upper() == "DEBUG":

    @event.listens_for(Engine, "before_cursor_execute")
    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        logger.debug("SQL: %s", statement.replace("\n", " ").strip())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_database():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
