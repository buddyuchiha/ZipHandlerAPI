from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile
import uvicorn

from core.logging import logger

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    logger.info("ZipHandlerAPI started")
    yield
    logger.info("ZipHandlerAPI stopped")


app = FastAPI(lifespan=app_lifespan)


@app.post("/upload")
async def upload_file(file: UploadFile) -> dict:
    return {"filename" : file.filename}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )