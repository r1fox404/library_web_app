from typing import List, TypeVar, Type

from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from core import OrmBase
from .authors.schemas import SAuthorCreate
from .books.schemas import SBookCreate
from .borrows.schemas import SBorrowCreate


ModelType = TypeVar("ModelType", bound=OrmBase)
SchemaType = TypeVar("SchemaType", SAuthorCreate, SBookCreate, SBorrowCreate)


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
        for name, value in input_schema.model_dump(exclude_unset=partial).items():
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


cruds = Crud()