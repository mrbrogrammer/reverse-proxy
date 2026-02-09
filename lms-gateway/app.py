from fastapi import FastAPI, Request, Depends
import uvicorn
from dotenv import load_dotenv
from exception.RouterNotFoundException import RouterNotFoundException
from router.usersRouter import UsersRouter


load_dotenv(".env.development")

app = FastAPI()

@app.api_route("{service_url:path}", methods=["GET", "POST", "DELETE", "PUT"])
async def gateway_route(request: Request, service_url: str, router: UsersRouter = Depends(UsersRouter)):

    response = await router.get_user(request=request)
    return response

@app.api_route("{service_url:path}", methods=["GET", "POST", "DELETE", "PUT"])
async def gateway_route_(request: Request, service_url: str, router: UsersRouter = Depends(UsersRouter)):

    response = await router.get_user(request=request)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
