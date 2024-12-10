from sqlalchemy.orm import Mapped

from .Base import OrmBase


class MAuthor(OrmBase):
    __tablename__ = "authors"
    
    first_name: Mapped[str]
    last_name: Mapped[str]
    birthday: Mapped[str]