"""Entry point del Loan Service."""
import logging
import time
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.config import settings
from app.database.database import SessionLocal, init_database
from app.api.routes import router as loans_router

logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    yield


def create_app(test_mode: bool = False) -> FastAPI:
    app = FastAPI(
        title=settings.APP_TITLE,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        lifespan=None if test_mode else lifespan,
        redirect_slashes=False,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(loans_router)

    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        elapsed = time.perf_counter() - start
        logger.info(
            "%s %s → %s (%.0fms)",
            request.method,
            request.url.path,
            response.status_code,
            elapsed * 1000,
        )
        return response

    @app.get("/health", tags=["health"])
    def health_check():
        return {"status": "ok"}

    @app.get("/ready", tags=["health"])
    def readiness_check():
        try:
            db = SessionLocal()
            db.execute(text("SELECT 1"))
            db.close()
            return {"status": "ok", "database": "connected"}
        except Exception as exc:
            logger.error("Readiness check failed: %s", exc)
            from fastapi import Response

            return Response(
                status_code=503,
                content=f'{{"status":"error","database":"{exc}"}}',
                media_type="application/json",
            )

    if test_mode:
        init_database()

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)
