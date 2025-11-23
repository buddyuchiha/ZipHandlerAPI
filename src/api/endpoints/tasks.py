from fastapi import APIRouter, Depends, HTTPException, UploadFile
from io import BytesIO

from api.dependencies.minio import get_minio_service

tasks_router = APIRouter()


@tasks_router.post("/upload")
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
