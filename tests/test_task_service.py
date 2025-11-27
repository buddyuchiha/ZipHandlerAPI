import pytest
from unittest.mock import AsyncMock, patch

from fastapi import UploadFile

from core.enums import TaskStatus
from schemas.dummy import SonarqubeResultScheme, BugsScheme, CodeSmellsScheme, VulnerabilitiesScheme
from schemas.tasks import ResultResponseScheme, UploadFileResponseScheme
from services.task_service import TaskService

@pytest.mark.asyncio
async def test_handle_result_success():
    mock_db = AsyncMock()
    
    mock_db.get_status.return_value = "completed"
    mock_db.get_results.return_value = SonarqubeResultScheme(
        overall_coverage=85.5,
        bugs=BugsScheme(total=5, critical=1, major=2, minor=2),
        code_smells=CodeSmellsScheme(total=10, critical=2, major=4, minor=4),
        vulnerabilities=VulnerabilitiesScheme(total=3, critical=1, major=1, minor=1)
    )
    
    result = await TaskService.handle_result("task_123", mock_db)
    
    assert isinstance(result, ResultResponseScheme)
    assert result.status == "completed"
    assert result.results.overall_coverage == 85.5
    assert result.results.bugs.total == 5
    assert result.results.bugs.critical == 1
    assert result.results.code_smells.total == 10
    assert result.results.vulnerabilities.total == 3
    
    mock_db.get_status.assert_called_once_with("task_123")
    mock_db.get_results.assert_called_once_with("task_123")


@pytest.mark.asyncio
async def test_handle_task_success():
    mock_file = AsyncMock(spec=UploadFile)
    mock_file.read.return_value = b"fake zip content"
    
    mock_minio = AsyncMock()
    mock_db = AsyncMock()
    mock_user = "test_user"
    
    with patch('services.task_service.FileService.handle_file', AsyncMock()) as mock_handle_file, \
         patch('services.task_service.DummyAnalysisService.analyze_sonarqube', AsyncMock()) as mock_analyze, \
         patch('services.task_service.uuid.uuid4') as mock_uuid:
        
        mock_uuid.return_value = "test-uuid-123"
        
        mock_analyze.return_value = {"coverage": 85, "bugs": 5}
        
        result = await TaskService.handle_task(mock_file, mock_minio, mock_user, mock_db)
        
        assert isinstance(result, UploadFileResponseScheme)
        assert result.task_id == "test-uuid-123"
        
        mock_db.update_status.assert_any_call("test-uuid-123", TaskStatus.IN_PROGRESS)
        mock_db.create.assert_called_once_with("test-uuid-123", "test_user")
        mock_db.update_result.assert_called_once_with("test-uuid-123", {"coverage": 85, "bugs": 5})
        mock_db.update_status.assert_any_call("test-uuid-123", TaskStatus.SUCCESS)
        
        mock_handle_file.assert_called_once()
        mock_minio.put_file.assert_called_once_with(mock_file)
        mock_analyze.assert_called_once_with(b"fake zip content")
        
        mock_file.read.assert_called_once()