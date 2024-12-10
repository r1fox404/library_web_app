from fastapi import FastAPI


fastapi_app = FastAPI(
    title="Some library`s web-application"
)


@fastapi_app.get("/")
async def homepage():
    return {"message": "This is a home page"}