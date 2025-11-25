from io import BytesIO
import uuid

from fastapi import UploadFile, Depends
from minio import Minio
from repositories.task_repository import TasksReposity


class TaskService:
    @staticmethod
    async def load_file():
        pass 
    
    @staticmethod
    async def create_task():
        pass 
    
    @staticmethod
    async def analyze_code():
        pass 
    
    @staticmethod
    async def find_vulnerabilities():
        pass 
    
    @staticmethod
    async def find_bugs():
        pass 
    
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
        
        content = BytesIO(file_data) 
        
        minio.put_file(
            content,
            file.filename,
            len(file_data)
        )
        
        await db.create(str(uuid.uuid4()), user)
        
        
        