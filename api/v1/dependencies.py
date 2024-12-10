from typing import Annotated, Type

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api import cruds, ModelType
from core import db_conn


class SDepends:
    
    @classmethod
    async def item_by_id(
        cls,
        *,
        id: Annotated[int, Path],
        input_model: Type[ModelType],
        session: AsyncSession = Depends(db_conn.scoped_session),
    ) -> ModelType:
        item = await cruds.get_by_id(
            session=session,
            input_model=input_model,
            id=id
        )
        if item is not None:
            return item


model_depend = SDepends()