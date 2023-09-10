from fastapi import FastAPI
from core.config import settings
from pymongo import MongoClient
from api.router import router
db = MongoClient(settings.MONGO_CONNECTION_STRING)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.get("/")
def root():
    return {"message": "Hello World with Fastapi"}

app.include_router(router, prefix=settings.API_V1_STR)