from pydantic import BaseModel

from schemas.dummy import SonarqubeResultScheme

  
class ResultResponseScheme(BaseModel):
    """Analysis results response"""
    
    status: str
    results: SonarqubeResultScheme
    
    
class UploadFileResponseScheme(BaseModel):
    """File upload response"""
    
    task_id: str