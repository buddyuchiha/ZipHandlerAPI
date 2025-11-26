from io import BytesIO

from fastapi import APIRouter, Depends, HTTPException, UploadFile

from api.dependencies.minio import get_minio_service
from api.dependencies.auth import get_current_user
from api.dependencies.database import get_tasks_repository
from core.logging import logger
from repositories.task_repository import TasksRepository
from services.task_service import TaskService
from schemas.tasks import ResultResponseScheme, UploadFileResponseScheme

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
    minio=Depends(get_minio_service), 
    user=Depends(get_current_user),
    db: TasksRepository=Depends(get_tasks_repository)
    ) -> UploadFileResponseScheme:
    return await TaskService.handle_task(file, minio, user, db)

@archive_router.get(
    "/results/{task_id}",
    summary="Get Result after handling", 
    tags=["Archive Router Endpoints"]
    )
async def get_results(
    task_id: str, 
    db: TasksRepository = Depends(get_tasks_repository),
    user=Depends(get_current_user)
    ) -> ResultResponseScheme: 
    return await TaskService.handle_result(task_id, db)