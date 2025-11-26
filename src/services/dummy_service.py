# services/dummy_services.py
import asyncio
import random

from schemas.dummy import (
    BugsScheme,
    CodeSmellsScheme,
    VulnerabilitiesScheme,
    SonarqubeResultScheme
)

class DummyAnalysisService:  
    async def get_bugs(self, file_content: bytes) -> BugsScheme:
        await asyncio.sleep(0.5)
        
        return BugsScheme(
            total=random.randint(0, 20),
            critical=random.randint(0, 3),
            major=random.randint(0, 7),
            minor=random.randint(0, 10)
        )
        
    async def get_code_smells(self, file_content: bytes) -> CodeSmellsScheme:
        await asyncio.sleep(0.5)
        
        return CodeSmellsScheme(
            total=random.randint(0, 30),
            critical=random.randint(0, 5),
            major=random.randint(0, 10),
            minor=random.randint(0, 15)
        )
    
    async def get_vulnerabilities(self, file_content: bytes) -> VulnerabilitiesScheme:
        await asyncio.sleep(0.5)
        
        return VulnerabilitiesScheme(
            total=random.randint(0, 8),
            critical=random.randint(0, 2),
            major=random.randint(0, 3),
            minor=random.randint(0, 3)
        )
        
      
    async def analyze_sonarqube(self, file_content: bytes) -> SonarqubeResultScheme:
        bugs, code_smells, vulnreabilities= await asyncio.gather(
            self.get_bugs(file_content),
            self.get_code_smells(file_content),
            self.get_vulnerabilities(file_content)
        )
        
        return SonarqubeResultScheme(
            overall_coverage=random.uniform(50.0, 95.0), 
            bugs=bugs,
            code_smells=code_smells,
            vulnerabilities=vulnreabilities
        )