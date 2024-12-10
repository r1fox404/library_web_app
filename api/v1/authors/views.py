from typing import Annotated, List

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from api import cruds, model_depend
from core import (
    MAuthor,
    db_conn
)
from .schemas import (
    SAuthor,
    SAuthorCreate,
    SAuthorUpdate,
    SAuthorUpdatePartial
)


router = APIRouter(tags=["Authors"])


@router.get("/", response_model=List[SAuthor], status_code=status.HTTP_200_OK)
async def get_authors(
    session: AsyncSession = Depends(db_conn.scoped_session)
):
    authors = await cruds.get_all(session=session, input_model=MAuthor)
    if not authors:
        raise HTTPException(status_code=404, detail="Authors not found.")
    return authors


@router.get("/{author_id}", response_model=SAuthor, status_code=status.HTTP_200_OK)
async def get_author_by_id(
    author: SAuthor = Depends(model_depend.item_by_id)
):
    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")
    return author


@router.post("/", response_model=SAuthor, status_code=status.HTTP_201_CREATED)
async def add_author(
    author: Annotated[SAuthorCreate, Depends()],
    session: AsyncSession = Depends(db_conn.scoped_session)
):
    return await cruds.create(
        session=session,
        input_model=MAuthor,
        input_schema=author
    )


@router.put("/{author_id}", response_model=SAuthor, status_code=status.HTTP_200_OK)
async def update_author(
    author_in: Annotated[SAuthorUpdate, Depends()],
    author: SAuthor = Depends(model_depend.item_by_id),
    session: AsyncSession = Depends(db_conn.scoped_session)
):
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return await cruds.update(
        session=session,
        input_model=MAuthor,
        input_schema=author_in
    )


@router.patch("/{author_id}", response_model=SAuthor, status_code=status.HTTP_200_OK)
async def update_author_partial(
    author_in: Annotated[SAuthorUpdatePartial, Depends()],
    author: SAuthor = Depends(model_depend.item_by_id),
    session: AsyncSession = Depends(db_conn.scoped_session)
):
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return await cruds.update(
        session=session,
        input_model=MAuthor,
        input_schema=author_in,
        partial=True
    )


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(
    author: SAuthor = Depends(model_depend.item_by_id),
    session: AsyncSession = Depends(db_conn.scoped_session)
):
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return await cruds.delete(
        session=session,
        input_model=author
    )