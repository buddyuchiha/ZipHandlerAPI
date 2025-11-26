from sqlalchemy import select, delete, update

from core.enums import TaskStatus
from models.models import TasksORM
from schemas.dummy import SonarqubeResultScheme


class TasksRepository:
    def __init__(self, session) -> None:
        self.session = session
        
    async def create(self, id: str, user_id: str) -> TasksORM:
        async with self.session as session:
            task = TasksORM(id=id, user_id=user_id)
            session.add(task)
            
            await session.commit()
            await session.refresh(task)
            
            return task.id 
        
    async def get_status(self, task_id: str) -> str: 
        async with self.session as session: 
            query = (select(
                TasksORM.status 
                )
                .where(TasksORM.id == task_id)
            )
            
            result = await session.execute(query)
            
            return result.scalar_one_or_none()
        
    async def update_result(
        self, 
        id: str, 
        data: SonarqubeResultScheme
        ) -> None:
        async with self.session as session:
            query = (update(
                TasksORM    
                )
                .where(TasksORM.id == id)
                .values(result=data.model_dump())
            )
            
            await session.execute(query)
            await session.commit()
            
    async def update_status(self, id: str, status: TaskStatus) -> None:
        async with self.session as session:
            query = (update(
                    TasksORM
                    )
                    .where(TasksORM.id == id)
                    .values(status=status)
            )
            
            await session.execute(query)
            await session.commit()
            
    async def get_results(self, id: str) -> dict:
        async with self.session as session:
            query = (select(
                    TasksORM.result
                    )
                    .where(TasksORM.id == id)
            )
            
            result = await session.execute(query)
            
            return result.scalar_one_or_none()