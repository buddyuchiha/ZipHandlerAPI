from io import BytesIO

from fastapi import APIRouter, Depends, HTTPException, UploadFile

from api.dependencies.minio import get_minio_service
from api.dependencies.auth import get_current_user
from core.logging import logger


archive_router = APIRouter(
    tags=["Archive Router Endpoints"]
    )

@archive_router.post(
    "/upload",
    summary="Download ZIP-archive to the MinIO",
    tags=["Archive Router Endpoints"]
    )
async def upload_file(
    file: UploadFile, 
    minio = Depends(get_minio_service), 
    used = Depends(get_current_user)
    ) -> dict:
    file_data = await file.read()

    content = BytesIO(file_data)
    
    await minio.put_file(
        content,
        file.filename,
        len(file_data)
    )

    return {"filename" : file.filename}
