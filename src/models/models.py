from datetime import datetime

from sqlalchemy import Enum, func, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from core.enums import TaskStatus
from database.base import Base


class TasksORM(Base):
    """ORM Class to describe the table"""
    
    __tablename__ = "tasks"
    
    id: Mapped[str] = mapped_column(
        primary_key=True
        )
    user_id: Mapped[str]
    status: Mapped[str] = mapped_column(
        Enum(TaskStatus), 
        default=TaskStatus.PENDING
        )
    result: Mapped[dict] = mapped_column(
        JSON,
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column( 
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )