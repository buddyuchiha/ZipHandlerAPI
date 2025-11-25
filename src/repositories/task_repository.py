from sqlalchemy import select, delete, update

from models.models import TasksORM

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
        
    async def get_single(self, task_id: str) -> str: 
        async with self.session as session: 
            query = (select(
                TasksORM.status 
                ).where(TasksORM.id == task_id)
            )
            
            result = await session.execute(query)
            
            return result.scalars().all()