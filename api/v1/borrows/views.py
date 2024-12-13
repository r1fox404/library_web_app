from typing import Annotated, List

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from core import db_conn, MBorrow
from .cruds import get_all, create
from .depends import borrow_by_id
from .schemas import (
    SBorrow,
    SBorrowCreate,
    SBorrowReturn
)


router = APIRouter(tags=["Borrows"])


@router.get("", response_model=List[SBorrow], status_code=status.HTTP_200_OK)
async def get_borrows(
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    books = await get_all(
        session=session,
        model=MBorrow)
    
    if not books:
        raise HTTPException(status_code=404, detail="Borrows not found.")
    
    return books


@router.get("/{id}", response_model=SBorrow, status_code=status.HTTP_200_OK)
async def get_borrow_by_id(
    borrow: Annotated[SBorrow, Depends(borrow_by_id)]
):
    return borrow


@router.post("", response_model=SBorrow, status_code=status.HTTP_201_CREATED)
async def add_book(
    book_schema: Annotated[SBorrowCreate, Depends()],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):  
    try:
        item = await create(
            session=session,
            model=MBorrow,
            schema=book_schema
        )
    except ValueError:
        raise HTTPException(status_code=404, detail="Book does not exist or count over")
    
    return item