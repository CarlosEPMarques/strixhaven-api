from collections.abc import AsyncGenerator
import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from src.main import app
from src.settings.database.sqlalchemy import SessionLocal
from src.settings.jwt.jwt_service import create_session


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient]:
    user_data = {"user_id": 1, "username": "testuser"}
    token = create_session(user_data)
    headers = {"Authorization": f"Bearer {token}"}
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test', headers=headers) as client:
        yield client

@pytest.fixture(scope='session')
async def session() -> AsyncGenerator[AsyncSession]:
    session = SessionLocal()
    try:
        yield session
    finally:
        await session.close()