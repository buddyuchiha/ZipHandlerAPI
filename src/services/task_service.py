import asyncio
from io import BytesIO
import uuid

from fastapi import UploadFile, Depends
from minio import Minio

from repositories.task_repository import TasksReposity
from services.file_service import FileService
from services.dummy_service import DummyAnalysisService


class TaskService:
    @staticmethod
    async def load_file():
        pass 
    
    @staticmethod
    async def create_task(user, db, ):
        await db.create(str(uuid.uuid4()), user)
    
    @staticmethod
    async def get_result(task_id: str, db: TasksReposity):
        return await db.get_single(task_id) 
    
    @staticmethod
    async def handle_task(
        file: UploadFile, 
        minio: Minio, 
        user: str, 
        db: TasksReposity
        ):
        file_data = await file.read()        
        
        for file_content in file_data: 
            pass 
            
        content = BytesIO(file_data) 
        
        minio.put_file(
            content,
            file.filename,
            len(file_data)
        )
        
        await db.create(str(uuid.uuid4()), user)
        
        
        