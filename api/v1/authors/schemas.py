from pydantic import BaseModel


class SAuthorBase(BaseModel):

    first_name: str
    last_name: str
    birthday: str


class SAuthorCreate(SAuthorBase):
    pass


class SAuthorUpdate(SAuthorCreate):
    pass


class SAuthorUpdatePartial(SAuthorCreate):

    first_name: str | None = None
    last_name: str | None = None
    birthday: str | None = None


class SAuthor(SAuthorBase):

    id: int