import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter

from routes import router


load_dotenv()

app = FastAPI()

api_router = APIRouter(prefix="/api/v0")
api_router.include_router(router)

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app", host="localhost", port=8000, log_level="info", reload=True
    )
