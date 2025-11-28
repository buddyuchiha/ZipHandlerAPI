import asyncio
from io import BytesIO
import uuid

from fastapi import UploadFile
from minio import Minio

from core.enums import TaskStatus
from core.logging import logger
from repositories.task_repository import TasksRepository
from services.file_service import FileService
from services.dummy_service import DummyAnalysisService
from schemas.tasks import ResultResponseScheme, UploadFileResponseScheme


class TaskService:
    """Service for task processing operations"""
    
    @staticmethod
    async def handle_result(
        task_id: str, 
        db: TasksRepository
    ) -> ResultResponseScheme:
        """Get task results from database"""
        status = await db.get_status(task_id)
        results = await db.get_results(task_id)
        
        logger.info(f"Got results from handle_result: {results}")
        
        return ResultResponseScheme(
            status=status, 
            results=results
        ) 

    @staticmethod
    async def handle_task(
        file: UploadFile, 
        minio: Minio, 
        user: str, 
        db: TasksRepository
    ) -> UploadFileResponseScheme:
        """Handle file upload and analysis process"""
        file_data = await file.read()        
        content = BytesIO(file_data)
        id = str(uuid.uuid4())
        await file.seek(0)

        await db.update_status(id, TaskStatus.IN_PROGRESS)

        FileService.handle_file(file, file_data, content)

        *_, result = await asyncio.gather(
            db.create(id, user),
            minio.put_file(file), 
            DummyAnalysisService.analyze_sonarqube(file_data), 
        )
        
        await db.update_result(id, result)
        await db.update_status(id, TaskStatus.SUCCESS)
        
        logger.info(f"Task handled, task_id: {id}")
        
        return UploadFileResponseScheme(
            task_id=id
        )