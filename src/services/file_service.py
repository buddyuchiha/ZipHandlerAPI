from io import BytesIO
from zipfile import ZipFile

from fastapi import UploadFile, HTTPException

from core.config import settings

class FileService:
    @staticmethod
    def check_integrity(content: BytesIO) -> None:
        try:
            with ZipFile(content, 'r') as zip_obj:
                corrupt_file = zip_obj.testzip()
                if corrupt_file:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Damaged data in ZipFile: {corrupt_file}"
                    )
        except Exception as e:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid ZipFile: {str(e)}"
            )
            
    @staticmethod
    def check_size(file_data: bytes) -> None:
        if len(file_data) > settings.calculate_file_size():
            raise HTTPException(
                status_code=400,
                detail=f"File must be > {settings.calculate_file_size()}"
                )
    
    @staticmethod
    def check_format(file: UploadFile) -> None:
        if not file.filename.endswith(".zip"):
            raise HTTPException(
                status_code=400,
                detail="File must be ZIP format"
                )
    
    @staticmethod
    async def handle_file(file: UploadFile):
        FileService.check_format(file)
        
        file_data = await file.read()        
        FileService.check_size(file_data)
        
        content = BytesIO(file_data) 
        FileService.check_integrity(content)
        
        content.seek(0)

        # await minio.put_file(
        #     content,
        #     file.filename,
        #     len(file_data)
        # )  