from fastapi import FastAPI, Request, HTTPException
import httpx
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv(".env.development")

app = FastAPI()

# LMS_USERS_SERVICE_URL = os.getenv("LMS_USERS_SERVICE_URL", "http://localhost:8001")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
