from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from api.v1.books.schemas import SBook


class SAuthorBase(BaseModel):

    first_name: str
    last_name: str
    birthday: str


class SAuthorCreate(SAuthorBase):
    pass


class SAuthorUpdate(SAuthorCreate):
    pass


class SAuthorUpdatePartial(SAuthorCreate):

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birthday: Optional[str] = None


class SAuthor(SAuthorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class SAuthorView(SAuthor):
    books: Optional[List[SBook]]