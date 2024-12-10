from typing import List, Type, TypeVar

from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from core import OrmBase
from .authors.schemas import SAuthorUpdate, SAuthorUpdatePartial
from .books.schemas import SBookUpdate, SBookUpdatePartial
from .borrows.schemas import SBorrowUpdate, SBorrowUpdatePartial


ModelType = TypeVar("OrmModel", bound=OrmBase)
SchemaType = TypeVar(
    "PydanticSchema", 
    SAuthorUpdate, SAuthorUpdatePartial,
    SBookUpdate, SBookUpdatePartial,
    SBorrowUpdate, SBorrowUpdatePartial
)


class Crud:
    
    @classmethod
    async def get_all(
        cls,
        *,
        session: AsyncSession,
        input_model: Type[ModelType]
    ) -> List[ModelType]:
        stmt = select(input_model)
        result: Result = await session.execute(statement=stmt)
        items = result.scalars().all()
        return items
    
    
    @classmethod
    async def get_by_id(
        cls,
        *,
        session: AsyncSession,
        input_model: Type[ModelType],
        id: int
    ) -> ModelType:
        return await session.get(input_model, id)
    
    
    @classmethod
    async def create(
        cls,
        *,
        session: AsyncSession,
        input_model: Type[ModelType],
        input_schema: SchemaType
    ) -> ModelType:
        item = input_model(**input_schema.model_dump())
        session.add(item)
        await session.commit()
        return item
    
    
    @classmethod
    async def update(
        cls,
        *,
        session: AsyncSession,
        input_model: Type[ModelType],
        input_schema: SchemaType,
        partial: bool = False
    ) -> ModelType:
        for name, value in input_schema.model_dump(exclude_none=partial).items():
            setattr(input_model, name, value)
        await session.commit()
        return input_model
    
    
    @classmethod
    async def delete(
        cls, 
        *,
        session: AsyncSession,
        input_model: Type[ModelType]
    ):
        await session.delete(input_model)
        await session.commit()