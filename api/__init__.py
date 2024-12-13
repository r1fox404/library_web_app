from fastapi import APIRouter

from .v1.authors.views import router as authors_router
from .v1.books.views import router as books_router
from .v1.borrows.views import router as borrow_router


api_router = APIRouter()
api_router.include_router(router=authors_router, prefix="/authors")
api_router.include_router(router=books_router, prefix="/books")
api_router.include_router(router=borrow_router, prefix="/borrows")