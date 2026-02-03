from fastapi import Depends, FastAPI, Request
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from router.users_route import router
from config.database import Base
from config.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
