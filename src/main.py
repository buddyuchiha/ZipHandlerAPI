from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
import uvicorn

from api.endpoints.tasks import tasks_router
from api.dependencies.auth import get_current_user
from core.config import settings
from core.logging import logger

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    logger.info("ZipHandlerAPI started")
    yield
    logger.info("ZipHandlerAPI stopped")


app = FastAPI(lifespan=app_lifespan)

app.include_router(tasks_router)

@app.get("/")
async def keycloak_test():
    pass 

@app.get("/user")  
async def current_users(user: dict = Depends(get_current_user)):
    return user

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True
    )