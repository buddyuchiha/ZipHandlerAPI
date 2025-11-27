import asyncio
import random

from schemas.dummy import (
    BugsScheme,
    CodeSmellsScheme,
    VulnerabilitiesScheme,
    SonarqubeResultScheme
)


class DummyAnalysisService:  
    """Dummy service for code analysis simulation"""
    
    @staticmethod
    async def get_bugs(file_content: bytes) -> BugsScheme:
        """Generate random bugs analysis"""
        await asyncio.sleep(0.5)
        
        return BugsScheme(
            total=random.randint(0, 20),
            critical=random.randint(0, 3),
            major=random.randint(0, 7),
            minor=random.randint(0, 10)
        )
     
    @staticmethod   
    async def get_code_smells(file_content: bytes) -> CodeSmellsScheme:
        """Generate random code smells analysis"""
        await asyncio.sleep(0.5)
        
        return CodeSmellsScheme(
            total=random.randint(0, 30),
            critical=random.randint(0, 5),
            major=random.randint(0, 10),
            minor=random.randint(0, 15)
        )
    
    @staticmethod
    async def get_vulnerabilities(
        file_content: bytes
    ) -> VulnerabilitiesScheme:
        """Generate random security vulnerabilities"""
        await asyncio.sleep(0.5)
        
        return VulnerabilitiesScheme(
            total=random.randint(0, 8),
            critical=random.randint(0, 2),
            major=random.randint(0, 3),
            minor=random.randint(0, 3)
        )
        
    @staticmethod
    async def analyze_sonarqube(file_content: bytes) -> SonarqubeResultScheme:
        """Perform complete SonarQube analysis simulation"""
        bugs, code_smells, vulnreabilities= await asyncio.gather(
            DummyAnalysisService.get_bugs(file_content),
            DummyAnalysisService.get_code_smells(file_content),
            DummyAnalysisService.get_vulnerabilities(file_content)
        )
        
        return SonarqubeResultScheme(
            overall_coverage=random.uniform(50.0, 95.0), 
            bugs=bugs,
            code_smells=code_smells,
            vulnerabilities=vulnreabilities
        )