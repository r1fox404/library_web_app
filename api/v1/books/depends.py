from typing import Annotated

from fastapi import (
    Depends,
    Path,
    status,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from core import db_conn, MBook
from .cruds import get_by_id


async def book_by_id(
        id: Annotated[int, Path],
        session: Annotated[AsyncSession, Depends(db_conn.scoped_session)],
    ) -> MBook:
        item = await get_by_id(
            session=session,
            model=MBook,
            id=id
        )
        
        if item is not None:
            return item
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book by id {id} not found."
        )