import pytest

from services.dummy_service import DummyAnalysisService
from schemas.dummy import (
    BugsScheme,
    CodeSmellsScheme,
    VulnerabilitiesScheme,
    SonarqubeResultScheme
) 

@pytest.fixture
def dummy_service():
    return DummyAnalysisService()

@pytest.fixture
def file_content():
    return b"test"

@pytest.mark.asyncio
async def test_get_bugs(dummy_service, file_content):
    assert isinstance(
        await dummy_service.get_bugs(file_content), 
        BugsScheme
        )
    
@pytest.mark.asyncio 
async def test_get_code_smells(dummy_service, file_content):
    assert isinstance(
        await dummy_service.get_code_smells(file_content),
        CodeSmellsScheme
    )
    
@pytest.mark.asyncio
async def test_get_vulnerabilities(dummy_service, file_content):
    assert isinstance(
        await dummy_service.get_vulnerabilities(file_content),
        VulnerabilitiesScheme
    )  
    
@pytest.mark.asyncio 
async def test_sonarqube_coverage(dummy_service, file_content):
    result = await dummy_service.analyze_sonarqube(file_content)
    
    assert isinstance(
        result,
        SonarqubeResultScheme
    )  
    assert 50.0 <= result.overall_coverage <= 95.0