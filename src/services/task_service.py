import asyncio
from io import BytesIO
import uuid

from fastapi import UploadFile
from minio import Minio

from core.enums import TaskStatus
from repositories.task_repository import TasksRepository
from services.file_service import FileService
from services.dummy_service import DummyAnalysisService
from schemas.tasks import ResultResponseScheme, UploadFileResponseScheme


class TaskService:
    @staticmethod
    async def handle_result(
        task_id: str, 
        db: TasksRepository
        ) -> ResultResponseScheme:
        status = await db.get_status(task_id)
        results = await db.get_results(task_id)
        
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
        file_data = await file.read()        
        content = BytesIO(file_data)
        id = str(uuid.uuid4())
        await file.seek(0)

        await db.update_status(id, TaskStatus.IN_PROGRESS)

        *_, result = await asyncio.gather(
            FileService.handle_file(file, file_data, content),
            db.create(id, user),
            minio.put_file(file), 
            DummyAnalysisService.analyze_sonarqube(file_data), 
        )
        
        await db.update_result(id, result)
        await db.update_status(id, TaskStatus.SUCCESS)
        
        return UploadFileResponseScheme(
            task_id=id
        )