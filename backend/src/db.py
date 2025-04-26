from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from .settings import settings

# Create async engine
engine = create_async_engine(
    settings.database_url,
    echo=False,  # Set to True for SQL query logging
    pool_pre_ping=True,  # Enable connection health checks
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

@asynccontextmanager
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Provide a transactional scope around a series of operations.
    
    Yields:
        AsyncSession: Database session for performing operations
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def test_connection() -> int:
    """Test database connection by executing a simple query.
    
    Returns:
        int: Result of SELECT 1 query (should be 1)
        
    Raises:
        Exception: If database connection fails
    """
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        return result.scalar()