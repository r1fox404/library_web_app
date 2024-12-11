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
from core import db_conn, MAuthor
from .schemas import (
    SAuthor,
    SAuthorCreate,
    SAuthorUpdate,
    SAuthorUpdatePartial
)


router = APIRouter(tags=["Authors"])


@router.get("", response_model=List[SAuthor], status_code=status.HTTP_200_OK)
async def get_authors(
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    authors = await Crud.get_all(session=session, input_model=MAuthor)
    if not authors:
        raise HTTPException(status_code=404, detail="Authors not found.")
    return authors


@router.get("/{id}", response_model=SAuthor, status_code=status.HTTP_200_OK)
async def get_author_by_id(
    author: Annotated[SAuthor, Depends(SDepends.author)]
):
    return author


@router.post("", response_model=SAuthor, status_code=status.HTTP_201_CREATED)
async def add_author(
    author: Annotated[SAuthorCreate, Depends()],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await Crud.create(
        session=session,
        input_model=MAuthor,
        input_schema=author
    )


@router.put("/{id}", response_model=SAuthor)
async def update_author(
    author_in: Annotated[SAuthorUpdate, Depends()],
    author: Annotated[SAuthor, Depends(SDepends.author)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await Crud.update(
        session=session,
        input_model=author,
        input_schema=author_in
    )


@router.patch("/{id}", response_model=SAuthor)
async def update_author_partial(
    author_in: Annotated[SAuthorUpdatePartial, Depends()],
    author: Annotated[SAuthor, Depends(SDepends.author)],
    session: Annotated[AsyncSession, Depends(db_conn.scoped_session)]
):
    return await Crud.update(
        session=session,
        input_model=author,
        input_schema=author_in,
        partial=True
    )


@router.delete("/{id}")
async def delete_author(
    author: SAuthor = Depends(SDepends.author),
    session: AsyncSession = Depends(db_conn.scoped_session)
):
    return await Crud.delete(
        session=session,
        input_model=author
    )