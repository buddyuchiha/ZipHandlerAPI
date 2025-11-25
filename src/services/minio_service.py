from datetime import datetime
from io import BytesIO

from minio import Minio 

from core.config import settings
from core.logging import logger

class MinioService:
    def __init__(self) -> None:
        self.minio_url = self.minio_url = \
            f"{settings.MINIO_URL}:{settings.MINIO_API_PORT}"
        self.access_key = settings.MINIO_ACCESS_KEY
        self.secret_key = settings.MINIO_SECRET_KEY
        self.bucket_name = datetime.now().strftime("%Y%m%d")
        
        self.client = Minio(
            self.minio_url, 
            self.access_key,
            self.secret_key,
            secure=False
        )
        
        logger.info(
            f"Created client with url: {self.minio_url}"
            )
        
        self.make_bucket()
        
    def make_bucket(self) -> None:
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)
        
            logger.info(
            f"Created bucket with name: {self.bucket_name}"
            )
            
    async def put_file(self, file_data: BytesIO, file_name: str, file_size: int) -> None:                
        self.make_bucket()
        
        self.client.put_object(
            bucket_name=self.bucket_name,
            object_name=file_name,
            data=file_data,
            content_type="application/zip",
            length=file_size
        )
        
        logger.info(
            f"Added file {file_name} with len {file_size} to the MinIO"
            )
        
    