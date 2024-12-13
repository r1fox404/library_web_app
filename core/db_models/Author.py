from sqlalchemy.orm import Mapped, relationship

from .Base import OrmBase


class MAuthor(OrmBase):
    __tablename__ = "authors"
    
    first_name: Mapped[str]
    last_name: Mapped[str]
    birthday: Mapped[str]
    books = relationship("MBook", back_populates="author", cascade="all, delete-orphan", order_by="MBook.id")