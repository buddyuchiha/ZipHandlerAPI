from pydantic import BaseModel

from fastapi import UploadFile, File
from minio import Minio

from core.enums import TaskStatus
from schemas.dummy import SonarqubeResultScheme

  
class ResultResponseScheme(BaseModel):
    status: str
    results: SonarqubeResultScheme
    
    
class UploadFileResponseScheme(BaseModel):
    task_id: str