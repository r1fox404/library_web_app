from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from .Base import OrmBase


class MBook(OrmBase):
    __tablename__ = "books"
    
    name: Mapped[str]
    description: Mapped[str]
    count: Mapped[int]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    
    author = relationship("MAuthor", back_populates="books")
    borrows = relationship("MBorrow", order_by="MBorrow.id")