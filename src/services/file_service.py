from io import BytesIO
from zipfile import ZipFile

from fastapi import UploadFile, HTTPException

from core.config import settings
from core.logging import logger


class FileService:
    """Service for file validation operations"""
    
    @staticmethod
    def check_integrity(content: BytesIO) -> None:
        """Check ZIP file integrity"""
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
        """Check file size limit"""
        if len(file_data) > settings.calculate_file_size():
            raise HTTPException(
                status_code=400,
                detail="File size must be < 100 MB"
                )
    
    @staticmethod
    def check_format(file: UploadFile) -> None:
        """Check file format is ZIP"""
        if not file.filename.endswith(".zip"):
            raise HTTPException(
                status_code=400,
                detail="File must be ZIP format"
                )
    
    @staticmethod
    async def handle_file(
        file: UploadFile,
        file_data: bytes,
        content: bytes
    ) -> None:
        """Handle file validation process"""
        FileService.check_format(file)      
        FileService.check_size(file_data)
        content = BytesIO(file_data)
        FileService.check_integrity(content)
        
        logger.info(f"Handled file {file.filename}")