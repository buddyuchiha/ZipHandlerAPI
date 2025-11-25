from sqlalchemy import select, delete, update

from models.models import TasksORM

class TasksReposity:
    def __init__(self, session) -> None:
        self.session = session
        
    async def create(self, id: str) -> TasksORM:
        async with self.session as session:
            task = TasksORM(id)
            session.add(task)
            
            await session.commit()
            await session.refresh()
            
            return task 