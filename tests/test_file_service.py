from io import BytesIO
import pytest 

from fastapi import HTTPException, UploadFile

from services.file_service import FileService


@pytest.fixture
def file_service():
    return FileService()
    
@pytest.mark.asyncio
async def test_check_format(file_service):
    file = UploadFile(
        filename="document.pdf", 
        file=BytesIO(b"data")
    )
    
    with pytest.raises(HTTPException) as info:
        file_service.check_format(file)
        
    assert info.value.status_code == 400
    
@pytest.mark.asyncio 
async def test_check_size(file_service):
    file_data = b"x" * (100*1024*1024 + 1)
    
    with pytest.raises(HTTPException) as info:
        file_service.check_size(file_data)
        
    assert info.value.status_code == 400
    
@pytest.mark.asyncio 
async def test_check_integrity(file_service):
    content = BytesIO(b'BAD\x04' + b'x' * 100)
    
    with pytest.raises(HTTPException) as info:
        file_service.check_integrity(content)
        
    assert info.value.status_code == 400