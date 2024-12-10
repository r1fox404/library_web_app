from fastapi import FastAPI
from core import settings
from api import api_router


fastapi_app = FastAPI(
    title="Some library`s web-application"
)
fastapi_app.include_router(router=api_router, prefix=settings.api_v1_prefix)


@fastapi_app.get("/")
async def homepage():
    return {"message": "This is a home page :)"}