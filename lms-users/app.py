from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

USERS = ["L1", "L2"]

@app.get("/users")
async def users(request: Request):

    if "gateway-jwt-token" not in request.headers:
        return {
            "unauthorized" : "Unauthorized access"
        }
    
    return {
        "users" : USERS
    }
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
