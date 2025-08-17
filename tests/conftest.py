from typing import AsyncIterator
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest_asyncio.fixture
async def client() -> AsyncIterator[AsyncClient]:
    """
    Cliente HTTP assíncrono para testar a app FastAPI sem abrir porta,
    usando o ASGITransport do httpx.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
