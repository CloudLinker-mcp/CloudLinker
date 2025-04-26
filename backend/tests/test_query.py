"""Tests for the query endpoint."""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.main import app
from src.models.customer import Base
from src.db import get_db
from src.settings import settings

# Test database URL
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# Create test engine
engine = create_async_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create test session
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

@pytest.fixture
async def db_session():
    """Create a fresh database session for each test."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with TestingSessionLocal() as session:
        yield session
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def client(db_session):
    """Create a test client with a fresh database session."""
    async def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
    app.dependency_overrides.clear()

@pytest.mark.asyncio
async def test_query_with_valid_question(client):
    """Test querying with a valid question."""
    # Create a test customer first
    await client.post(
        "/customers",
        json={"name": "Test User", "email": "test@example.com"},
        headers={"X-API-Key": "test_key"}
    )
    
    # Query for all customers
    response = await client.post(
        "/query",
        json={"question": "show all customers"},
        headers={"X-API-Key": "test_key"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["sql"] == "SELECT * FROM customers"
    assert len(data["result"]) == 1
    assert data["result"][0]["name"] == "Test User"
    assert data["result"][0]["email"] == "test@example.com"

@pytest.mark.asyncio
async def test_query_with_invalid_question(client):
    """Test querying with an invalid question."""
    response = await client.post(
        "/query",
        json={"question": "invalid question"},
        headers={"X-API-Key": "test_key"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["sql"] == "-- TODO"
    assert data["result"] == []

@pytest.mark.asyncio
async def test_query_without_api_key(client):
    """Test querying without an API key."""
    response = await client.post(
        "/query",
        json={"question": "show all customers"}
    )
    
    assert response.status_code == 401
    assert response.json()["detail"] == "API key is missing"

@pytest.mark.asyncio
async def test_query_with_invalid_api_key(client):
    """Test querying with an invalid API key."""
    response = await client.post(
        "/query",
        json={"question": "show all customers"},
        headers={"X-API-Key": "invalid_key"}
    )
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API key" 