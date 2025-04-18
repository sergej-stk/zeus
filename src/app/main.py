from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    terms_of_service=settings.API_TERMS_OF_SERVICE,
    contact=settings.API_CONTACT,
    license_info=settings.API_LICENSE_INFO,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
