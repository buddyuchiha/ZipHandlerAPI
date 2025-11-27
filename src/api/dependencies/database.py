from fastapi import Depends 
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_db
from repositories.task_repository import TasksRepository


async def get_tasks_repository(
    session: AsyncSession=Depends(get_db)
) -> TasksRepository:
    """Creates and returns TasksRepository"""
    return TasksRepository(session)