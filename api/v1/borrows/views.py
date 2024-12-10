from typing import Annotated, List

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from api.v1.cruds import Crud
from api.v1.dependencies import SDepends
from core import db_conn, MBorrow
from .schemas import (
    SBorrow,
    SBorrowCreate,
    SBorrowUpdate,
    SBorrowUpdatePartial
)


router = APIRouter(tags=["Borrows"])


@router.get("/", response_model=List[SBorrow], status_code=status.HTTP_200_OK)
async def get_books(
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    books = await Crud.get_all(session=session, input_model=MBorrow)
    if not books:
        raise HTTPException(status_code=404, detail="Books not found.")
    return books


@router.get("/{id}/", response_model=SBorrow, status_code=status.HTTP_200_OK)
async def get_book_by_id(
    book: Annotated[SBorrow, Depends(SDepends.borrow)]
):
    return book


@router.post("/", response_model=SBorrow, status_code=status.HTTP_201_CREATED)
async def add_book(
    book: Annotated[SBorrow, Depends(SDepends.borrow)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await Crud.create(
        session=session,
        input_model=MBorrow,
        input_schema=book
    )


@router.put("/{id}/", response_model=SBorrow)
async def update_book(
    book_in: Annotated[SBorrowUpdate, Depends()],
    book: Annotated[SBorrow, Depends(SDepends.borrow)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await Crud.update(
        session=session,
        input_model=book,
        input_schema=book_in
    )


@router.patch("/{id}/", response_model=SBorrow)
async def update_book_partial(
    book_in: Annotated[SBorrowUpdatePartial, Depends()],
    book: Annotated[SBorrow, Depends(SDepends.borrow)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await Crud.update(
        session=session,
        input_model=book,
        input_schema=book_in,
        partial=True
    )


@router.delete("/{id}/")
async def delete_book(
    book: Annotated[SBorrow, Depends(SDepends.borrow)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await Crud.delete(
        session=session,
        input_model=book
    )