from pydantic import BaseModel


class BugsScheme(BaseModel): 
    """Bugs analysis results"""
    
    total: int 
    critical: int 
    major: int 
    minor: int 


class CodeSmellsScheme(BaseModel):
    """Code smells analysis results"""
    
    total: int 
    critical: int 
    major: int 
    minor: int 
    
    
class VulnerabilitiesScheme(BaseModel):
    """Security vulnerabilities results"""
    
    total: int 
    critical: int 
    major: int 
    minor: int 
    

class SonarqubeResultScheme(BaseModel):
    """SonarQube analysis results"""
    
    overall_coverage: float
    bugs: BugsScheme
    code_smells: CodeSmellsScheme
    vulnerabilities: VulnerabilitiesScheme