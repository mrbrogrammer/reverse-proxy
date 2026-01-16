import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# Database configuration from environment variables
ASYNC_DATABASE_URL = os.getenv("ASYNC_DATABASE_URL")

# Asynchronous engine
engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)

# Session maker
AsyncSessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

Base = declarative_base()


async def get_async_db():
    """ Dependency to get an async database session """
    async with AsyncSessionLocal() as session:
        yield session