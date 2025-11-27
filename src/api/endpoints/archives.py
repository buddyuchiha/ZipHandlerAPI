from fastapi import APIRouter, Depends, HTTPException, UploadFile

from api.dependencies.auth import get_current_user
from api.dependencies.database import get_tasks_repository
from api.dependencies.minio import get_minio_service
from core.logging import logger
from repositories.task_repository import TasksRepository
from services.minio_service import MinioService
from services.task_service import TaskService
from schemas.tasks import ResultResponseScheme, UploadFileResponseScheme

archive_router = APIRouter(
    tags=["Archive Router Endpoints"]
)

@archive_router.post(
    "/upload",
    summary="Download ZIP-archive to the MinIO",
    tags=["Archive Router Endpoints"], 
    status_code=201, 
    response_model=UploadFileResponseScheme
)
async def upload_file(
    file: UploadFile, 
    minio: MinioService = Depends(get_minio_service), 
    user: str = Depends(get_current_user),
    db: TasksRepository = Depends(get_tasks_repository)
) -> UploadFileResponseScheme:
    """
    Upload and handle ZIP archive
    
    Args:
        file: ZIP archive
        minio: MiniIO client
        user: Authenticated user ID from JWT token
        db: Database instance for database operations
        
    Returns:
        UploadFileResponseScheme: Task ID
    """
    logger.info(f"Upload request from user {user} for file: {file.filename}")
    
    try: 
        return await TaskService.handle_task(file, minio, user, db)
    except HTTPException: 
        raise
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"{e}"
        )
        
@archive_router.get(
    "/results/{task_id}",
    summary="Get Result after handling", 
    tags=["Archive Router Endpoints"], 
    response_model=ResultResponseScheme
)
async def get_results(
    task_id: str, 
    db: TasksRepository = Depends(get_tasks_repository),
    user: str = Depends(get_current_user)
) -> ResultResponseScheme: 
    """
    Get result from database by task id
    
    Args:
        taks_id: Task ID
        user: Authenticated user ID from JWT token
        db: Database instance for database operations
        
    Returns:
        ResultResponseScheme: Task status and result
    """    
    logger.info(f"Results request from user {user} for task: {task_id}")
    
    try: 
        return await TaskService.handle_result(task_id, db)
    except HTTPException:  
        raise
    except Exception:
        raise HTTPException(
            status_code=404, 
            detail="Задача не найдена"
        )