from contextlib import asynccontextmanager
from fastapi import Depends,FastAPI, UploadFile
from io import BytesIO
import uvicorn

from core.config import settings
from core.logging import logger
from dependencies.minio import get_minio_service

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    logger.info("ZipHandlerAPI started")
    yield
    logger.info("ZipHandlerAPI stopped")


app = FastAPI(lifespan=app_lifespan)

@app.post("/upload")
async def upload_file(
    file: UploadFile, 
    minio = Depends(get_minio_service)
    ) -> dict:
    file_data = BytesIO(await file.read())

    content = await file.read()
    
     
    await minio.put_file(
        file_data,
        file.filename,
        len(content)
    )
    
    return {"filename" : file.filename}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True
    )