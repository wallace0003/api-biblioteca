from typing import List
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Author(Base):
    __tablename__ = "author"

    id_author: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_name: Mapped[str] = mapped_column(String(60), nullable=False)

    books: Mapped[List["Book"]] = relationship(
        back_populates="author"
    )
