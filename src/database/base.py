import uuid
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, registry
from sqlalchemy.dialects.postgresql import UUID

engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@db:5434/postgres"
    )
session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            uuid.UUID: UUID(as_uuid=True)
        }
    )