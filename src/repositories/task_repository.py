from sqlalchemy import select, update

from core.enums import TaskStatus
from core.logging import logger
from models.models import TasksORM
from schemas.dummy import SonarqubeResultScheme


class TasksRepository:
    """Repository for task database operations"""
    
    def __init__(self, session) -> None:
        self.session = session
        
    async def create(self, id: str, user_id: str) -> str:
        """Create new task in database"""
        async with self.session as session:
            task = TasksORM(id=id, user_id=user_id)
            session.add(task)
            
            await session.commit()
            await session.refresh(task)
            
            logger.info(f"Created new task with id: {task.id}")
            
            return task.id 
        
    async def get_status(self, task_id: str) -> dict | None: 
        """Get task status by ID"""
        async with self.session as session: 
            query = (select(
                TasksORM.status 
                )
                .where(TasksORM.id == task_id)
            )
            
            result = await session.execute(query)
            
            logger.info(f"Got result for task: {task_id}")
            
            return result.scalar_one_or_none()
        
    async def update_result(
        self, 
        task_id: str, 
        data: SonarqubeResultScheme
    ) -> None:
        """Update task analysis results"""
        async with self.session as session:
            query = (update(
                TasksORM    
                )
                .where(TasksORM.id == task_id)
                .values(result=data.model_dump())
            )
            
            await session.execute(query)
            await session.commit()
            
            logger.info(f"Updated result for task: {task_id}")

            
    async def update_status(self, task_id: str, status: TaskStatus) -> None:
        """Update task status"""
        async with self.session as session:
            query = (update(
                    TasksORM
                    )
                    .where(TasksORM.id == task_id)
                    .values(status=status)
            )
            
            await session.execute(query)
            await session.commit()
            
            logger.info(f"Updated status for task: {task_id}")

            
    async def get_results(self, task_id: str) -> dict:
        """Get task analysis results"""
        async with self.session as session:
            query = (select(
                    TasksORM.result
                    )
                    .where(TasksORM.id == task_id)
            )
            
            result = await session.execute(query)
            
            logger.info(f"Got result for task: {task_id}")
            
            return result.scalar_one_or_none()