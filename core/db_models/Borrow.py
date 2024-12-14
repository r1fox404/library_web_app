from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .Base import OrmBase


class MBorrow(OrmBase):
    __tablename__ = "borrows"
    
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    readers_name: Mapped[str]
    issue_date: Mapped[str]
    return_date: Mapped[str]