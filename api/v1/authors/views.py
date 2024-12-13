from typing import Annotated, List

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from core import db_conn, MAuthor
from .cruds import get_all, create, update, delete
from .depends import author_by_id
from .schemas import (
    SAuthor,
    SAuthorView,
    SAuthorCreate,
    SAuthorUpdate,
    SAuthorUpdatePartial
)


router = APIRouter(tags=["Authors"])


@router.get("", response_model=List[SAuthorView], status_code=status.HTTP_200_OK)
async def get_authors(
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    authors = await get_all(
        session=session,
        model=MAuthor)
    
    if not authors:
        raise HTTPException(status_code=404, detail="Authors not found.")
    
    return authors


@router.get("/{id}", response_model=SAuthor, status_code=status.HTTP_200_OK)
async def get_author_by_id(
    author_schema: Annotated[SAuthor, Depends(author_by_id)]
):
    return author_schema


@router.post("", response_model=SAuthor, status_code=status.HTTP_201_CREATED)
async def add_author(
    author_schema: Annotated[SAuthorCreate, Depends()],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await create(
        session=session,
        model=MAuthor,
        schema=author_schema)


@router.put("/{id}", response_model=SAuthor)
async def update_author(
    author_schema: Annotated[SAuthorUpdate, Depends()],
    author_model: Annotated[SAuthor, Depends(author_by_id)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await update(
        session=session,
        model=author_model,
        schema=author_schema
    )


@router.patch("/{id}", response_model=SAuthor)
async def update_author_partial(
    author_schema: Annotated[SAuthorUpdatePartial, Depends()],
    author_model: Annotated[SAuthor, Depends(author_by_id)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await update(
        session=session,
        model=author_model,
        schema=author_schema,
        partial=True
    )


@router.delete("/{id}")
async def delete_author(
    author_model: Annotated[SAuthor, Depends(author_by_id)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await delete(
        session=session,
        model=author_model
    )