from io import BytesIO

from fastapi import UploadFile

from minio import Minio
from repositories.task_repository import TasksReposity


class TaskService:
    @staticmethod
    async def create_task(
        file: UploadFile, 
        minio: Minio, 
        user: str
        ):
        file_data = await file.read()        
        
        content = BytesIO(file_data) 
        
        await minio.put_object(
            content,
            file.filename,
            len(file_data)
        )
        
        