import os
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Database configuration from environment variables
ASYNC_DATABASE_URL = os.getenv("ASYNC_DATABASE_URL")

# Asynchronous engine
engine = create_engine("postgresql://admin:$tar&B3y0nd@localhost:5432/lms-users-dev", echo=True)

# postgresql://{username}:{password}@{host}:{port}/{database_name} 

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
