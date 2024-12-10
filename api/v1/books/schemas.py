from pydantic import BaseModel


class SBookBase(BaseModel):

    name: str
    description: str
    count: int
    author_id: int


class SBookCreate(SBookBase):
    pass


class SBookUpdate(SBookCreate):
    pass


class SBookUpdatePartial(SBookCreate):

    name: str | None = None
    description: str | None = None
    count: int | None = None
    author_id: int | None = None


class SBook(SBookBase):

    id: int