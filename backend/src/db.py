from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.settings import settings

engine = create_async_engine(settings.database_url.replace("postgresql://", "postgresql+asyncpg://"))
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def test_connection():
    async with engine.connect() as conn:
        result = await conn.execute("SELECT 1")
        return result.scalar()