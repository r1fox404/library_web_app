from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core import MBook, MAuthor
from .schemas import (
    SBookCreate,
    SBookUpdate,
    SBookUpdatePartial
)


async def get_all(
    session: AsyncSession,
    model: MBook
) -> List[MBook]:
    stmt = select(model).order_by(model.id)
    result = await session.execute(statement=stmt)
    items = result.unique().scalars().all()
    return items


async def get_by_id(
    session: AsyncSession,
    id: int,
    model: MBook,
) -> MBook:
    return await session.get(model, id)


async def create(
    session: AsyncSession,
    model: MBook,
    schema: SBookCreate
) -> MBook:
    stmt = select(MAuthor).filter(MAuthor.id == schema.author_id)
    result = await session.execute(statement=stmt)
    author = result.scalar_one_or_none()
    if not author:
        raise ValueError(f"Author by id {schema.author_id} not found.")
    item = model(**schema.model_dump())
    session.add(item)
    await session.commit()
    return item


async def update(
    session: AsyncSession,
    model: MBook,
    schema: SBookUpdate | SBookUpdatePartial,
    partial: bool = False
) -> MBook:
    if not partial:
        stmt = select(MAuthor).filter(MAuthor.id == schema.author_id)
        result = await session.execute(statement=stmt)
        author = result.scalar_one_or_none()
        if not author:
            raise ValueError(f"Author by id {schema.author_id} not found.")
    for name, value in schema.model_dump(exclude_none=partial).items():
        setattr(model, name, value)
    await session.commit()
    return model


async def delete(
    session: AsyncSession,
    model: MBook
) -> None:
    await session.delete(model)
    await session.commit()