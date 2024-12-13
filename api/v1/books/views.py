from typing import Annotated, List

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from core import db_conn, MBook
from api.v1.authors.depends import author_by_id
from .cruds import get_all, create, update, delete
from .depends import book_by_id
from .schemas import (
    SBook,
    SBookCreate,
    SBookUpdate,
    SBookUpdatePartial
)


router = APIRouter(tags=["Books"])


@router.get("", response_model=List[SBook], status_code=status.HTTP_200_OK)
async def get_books(
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    books = await get_all(
        session=session,
        model=MBook)
    
    if not books:
        raise HTTPException(status_code=404, detail="Books not found.")
    
    return books


@router.get("/{id}", response_model=SBook, status_code=status.HTTP_200_OK)
async def get_book_by_id(
    book: Annotated[SBook, Depends(book_by_id)]
):
    return book


@router.post("", response_model=SBook, status_code=status.HTTP_201_CREATED)
async def add_book(
    book_schema: Annotated[SBookCreate, Depends()],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):  
    try:
        item = await create(
            session=session,
            model=MBook,
            schema=book_schema
        )
    except ValueError:
        raise HTTPException(status_code=404, detail="Author does not exist")
    
    return item


@router.put("/{id}", response_model=SBook)
async def update_book(
    book_schema: Annotated[SBookUpdate, Depends()],
    book_model: Annotated[SBook, Depends(book_by_id)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    try:
        item = await update(
            session=session,
            model=book_model,
            schema=book_schema
        )
    except ValueError:
        raise HTTPException(status_code=404, detail="Author does not exist")
    
    return item


@router.patch("/{id}", response_model=SBook)
async def update_book_partial(
    book_schema: Annotated[SBookUpdatePartial, Depends()],
    book_model: Annotated[SBook, Depends(book_by_id)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    try:
        item = await update(
            session=session,
            model=book_model,
            schema=book_schema,
            partial=True
        )
    except ValueError:
        raise HTTPException(status_code=404, detail="Author does not exist")
    
    return item


@router.delete("/{id}")
async def delete_book(
    book_model: Annotated[SBook, Depends(book_by_id)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await delete(
        session=session,
        model=book_model
    )