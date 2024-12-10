from sqlalchemy.orm import Mapped

from .Base import OrmBase


class Borrow(OrmBase):
    __tablename__ = "borrows"
    
    book_id: Mapped[int]
    readers_name: Mapped[str]
    issue_date: Mapped[str]
    return_date: Mapped[str]