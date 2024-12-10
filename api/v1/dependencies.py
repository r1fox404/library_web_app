from typing import Annotated

from fastapi import Depends, Path, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.cruds import Crud
from core import db_conn, MAuthor, MBook, MBorrow


class SDepends:
    
    @classmethod
    async def author(
        cls,
        id: Annotated[int, Path],
        session: AsyncSession = Depends(db_conn.scoped_session),
    ) -> MAuthor:
        item = await Crud.get_by_id(
            session=session,
            input_model=MAuthor,
            id=id
        )
        if item is not None:
            return item
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author by id {id} not found."
        )
    
    
    @classmethod
    async def book(
        cls,
        id: Annotated[int, Path],
        session: AsyncSession = Depends(db_conn.scoped_session),
    ) -> MBook:
        item = await Crud.get_by_id(
            session=session,
            input_model=MBook,
            id=id
        )
        if item is not None:
            return item
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book by id {id} not found."
        )
    
    
    @classmethod
    async def book(
        cls,
        id: Annotated[int, Path],
        session: AsyncSession = Depends(db_conn.scoped_session),
    ) -> MBorrow:
        item = await Crud.get_by_id(
            session=session,
            input_model=MBorrow,
            id=id
        )
        if item is not None:
            return item
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Borrow by id {id} not found."
        )