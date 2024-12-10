from sqlalchemy.orm import Mapped

from .Base import OrmBase

class Book(OrmBase):
    __tablename__ = "books"
    
    name: Mapped[str]
    description: Mapped[str]
    count: Mapped[int]
    author_id: Mapped[int]