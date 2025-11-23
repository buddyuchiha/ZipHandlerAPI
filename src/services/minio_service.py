from datetime import datetime
from io import BytesIO

from minio import Minio 

from core.logging import logger

class MinioService:
    
    def __init__(self) -> None:
        self.minio_url = "localhost:9000"
        self.access_key = "minioadmin"
        self.secret_key = "minioadmin"
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
        self.client.put_object(
            bucket_name=str(self.bucket_name),
            object_name=file_name,
            data=file_data,
            content_type="application/pdf",
            length=file_size
        )
        
        
    