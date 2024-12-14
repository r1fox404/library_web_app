from pydantic import BaseModel, ConfigDict


class SBorrowBase(BaseModel):

    book_id: int
    readers_name: str
    issue_date: str
    return_date: str


class SBorrowCreate(SBorrowBase):
    pass


class SBorrowReturn(SBorrowCreate):
    
    return_date: str


class SBorrow(SBorrowBase):
    model_config = ConfigDict(from_attributes=True)

    id: int