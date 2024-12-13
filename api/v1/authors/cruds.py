from typing import List

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from core import MAuthor
from .schemas import (
    SAuthorCreate,
    SAuthorUpdate,
    SAuthorUpdatePartial
)


async def get_all(
    session: AsyncSession,
    model: MAuthor
) -> List[MAuthor]:
    stmt = select(model).order_by(model.id).options(joinedload(model.books))
    result = await session.execute(statement=stmt)
    items = result.unique().scalars().all()
    return items


async def get_by_id(
    session: AsyncSession,
    id: int,
    model: MAuthor,
) -> MAuthor:
    return await session.get(model, id)


async def create(
    session: AsyncSession,
    model: MAuthor,
    schema: SAuthorCreate
) -> MAuthor:
    item = model(**schema.model_dump())
    session.add(item)
    await session.commit()
    return item


async def update(
    session: AsyncSession,
    model: MAuthor,
    schema: SAuthorUpdate | SAuthorUpdatePartial,
    partial: bool = False
) -> MAuthor:
    for name, value in schema.model_dump(exclude_none=partial).items():
        setattr(model, name, value)
    await session.commit()
    return model


async def delete(
    session: AsyncSession,
    model: MAuthor
) -> None:
    await session.delete(model)
    await session.commit()