"""Configurazioni dell'applicazione tramite variabili d'ambiente."""
import os


class Settings:
    APP_TITLE: str = "Review Service"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Microservizio per la gestione delle recensioni"

    DATABASE_TYPE: str = os.getenv("DATABASE_TYPE", "sqlite")
    DATABASE_PATH: str = os.getenv("DATABASE_PATH", "/data/reviews.db")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/reviews",
    )
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # URL dei servizi dipendenti (inter-servizio)
    BOOK_SERVICE_URL: str = os.getenv("BOOK_SERVICE_URL", "http://book-service:8000")

    @property
    def DATABASE_HOST(self) -> str:
        return self.DATABASE_URL.split("@")[1].split(":")[0] if "@" in self.DATABASE_URL else "localhost"

    @property
    def sqlalchemy_url(self) -> str:
        if self.DATABASE_TYPE == "postgres":
            return self.DATABASE_URL
        return f"sqlite:///{self.DATABASE_PATH}"


settings = Settings()
