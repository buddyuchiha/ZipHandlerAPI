from pydantic import BaseModel


class BugsScheme(BaseModel): 
    total    : int 
    critical : int 
    major    : int 
    minor    : int 


class CodeSmellsScheme(BaseModel):
    total    : int 
    critical : int 
    major    : int 
    minor    : int 
    
    
class VulnerabilitiesScheme(BaseModel):
    total    : int 
    critical : int 
    major    : int 
    minor    : int 
    

class SonarqubeResultScheme(BaseModel):
    overall_coverage : float
    bugs             : BugsScheme
    code_smells      : CodeSmellsScheme
    vulnerabilities  : VulnerabilitiesScheme 
     