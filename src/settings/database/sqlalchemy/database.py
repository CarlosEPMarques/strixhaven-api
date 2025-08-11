from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.schema import MetaData
from src.settings.database import database_settings

engine = create_async_engine(database_settings.postgresql_url)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    metadata = MetaData(schema='public')
    
async def get_session() -> AsyncGenerator[AsyncSession]:
    session = SessionLocal()
    try:
        yield session
    finally:
        await session.close()