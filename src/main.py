from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from api.endpoints.tasks import tasks_router
from core.config import settings
from core.logging import logger

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    logger.info("ZipHandlerAPI started")
    yield
    logger.info("ZipHandlerAPI stopped")


app = FastAPI(lifespan=app_lifespan)

app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True
    )