"""Configurazioni dell'applicazione tramite variabili d'ambiente."""
import os


class Settings:
    APP_TITLE: str = "Book Service"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Microservizio per la gestione dei libri"

    DATABASE_TYPE: str = os.getenv("DATABASE_TYPE", "sqlite")

    # SQLite
    DATABASE_PATH: str = os.getenv("DATABASE_PATH", "/data/books.db")

    # PostgreSQL
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/books",
    )

    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @property
    def DATABASE_HOST(self) -> str:
        """Estrae l'host dalla DATABASE_URL."""
        return self.DATABASE_URL.split("@")[1].split(":")[0] if "@" in self.DATABASE_URL else "localhost"

    @property
    def sqlalchemy_url(self) -> str:
        """Restituisce la connection string SQLAlchemy corretta per il DB in uso."""
        if self.DATABASE_TYPE == "postgres":
            return self.DATABASE_URL
        return f"sqlite:///{self.DATABASE_PATH}"


settings = Settings()
