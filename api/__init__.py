from fastapi import APIRouter

from .v1.authors.views import router as authors_router
from .v1.dependencies import SDepends
from .v1.cruds import (
    Crud,
    ModelType,
    SchemaType
)

api_router = APIRouter()
api_router.include_router(router=authors_router, prefix="/authors")