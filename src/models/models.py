from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Enum, func, JSON, DateTime, text
from sqlalchemy.dialects.postgresql import UUID as UUIDType
from sqlalchemy.orm import Mapped, mapped_column

from core.enums import TaskStatus
from database.base import Base


class TasksORM(Base):
    __tablename__ = "tasks"
    
    id: Mapped[UUID] = mapped_column(
        UUIDType(as_uuid=True),
        primary_key=True,
        default=uuid4,
        server_default=text("gen_random_uuid()")
        )
    user_id: Mapped[UUID]  = mapped_column(
        UUIDType(as_uuid=True),
        default=uuid4,
        nullable=True,
        )
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