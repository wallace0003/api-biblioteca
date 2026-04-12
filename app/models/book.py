from datetime import datetime
from typing import List

from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Book(Base):
    __tablename__ = "book"

    id_book: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[datetime] = mapped_column(DateTime)

    id_author: Mapped[int] = mapped_column(
        ForeignKey("author.id_author"),
        nullable=False
    )


    author: Mapped["Author"] = relationship(
        back_populates="books"
    )
