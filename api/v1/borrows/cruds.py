from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.books.schemas import SBookUpdatePartial
from core import MBorrow, MBook
from .schemas import (
    SBorrowCreate,
    SBorrowReturn,
)


async def get_all(
    session: AsyncSession,
    model: MBorrow
) -> List[MBorrow]:
    stmt = select(model).order_by(model.id)
    result = await session.execute(statement=stmt)
    items = result.unique().scalars().all()
    return items


async def get_by_id(
    session: AsyncSession,
    id: int,
    model: MBorrow,
) -> MBorrow:
    return await session.get(model, id)



async def create(
    session: AsyncSession,
    model: MBorrow,
    schema: SBorrowCreate
) -> MBorrow:
    stmt = select(MBook).filter(MBook.id == schema.book_id, MBook.count > 0)
    result = await session.execute(statement=stmt)
    book = result.scalar_one_or_none()
    if not book:
        raise ValueError(f"Book by id {schema.book_id} not found or book over.")
    item = model(**schema.model_dump())
    book.count -= 1
    session.add(book)
    session.add(item)
    await session.commit()
    return item


# async def update(
#     session: AsyncSession,
#     model: MBook,
#     schema: SBookUpdate | SBookUpdatePartial,
#     partial: bool = False
# ) -> MBook:
#     stmt = select(MAuthor).filter(MAuthor.id == schema.author_id)
#     result = await session.execute(statement=stmt)
#     author = result.scalar_one_or_none()
#     if not author:
#         raise ValueError(f"Author by id {schema.author_id} not found.")
#     for name, value in schema.model_dump(exclude_none=partial).items():
#         setattr(model, name, value)
#     await session.commit()
#     return model


# async def delete(
#     session: AsyncSession,
#     model: MBook
# ) -> None:
#     await session.delete(model)
#     await session.commit()