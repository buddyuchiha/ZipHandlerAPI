import datetime
import uuid
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class TasksORM(Base):
    __tablename__ = "tasks"