from fastapi import Depends, FastAPI, Request
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_async_db
from router import users

app = FastAPI()

USERS = ["L4", "L2"]

@app.get("/users")
async def users(request: Request, db: AsyncSession = Depends(get_async_db)):

    get_users_query = await db.execute("SELECT * FROM users")
    users = get_users_query.fetchall()
    print(users)

    if "gateway-jwt-token" not in request.headers:
        return {
            "unauthorized" : "Unauthorized access"
        }
    
    return {
        "users" : USERS
    }

app.include_router(users.router)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
