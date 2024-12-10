from pydantic import BaseModel


class SBorrowBase(BaseModel):

    book_id: int
    readers_name: str
    issue_date: str
    return_date: str


class SBorrowCreate(SBorrowBase):
    pass


class SBorrowUpdate(SBorrowCreate):
    pass


class SBorrowUpdatePartial(SBorrowCreate):
    
    book_id: int | None = None
    readers_name: str | None = None
    issue_date: str | None = None
    return_date: str | None = None


class SBorrow(SBorrowBase):

    id: int