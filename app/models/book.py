from typing import List

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Book(Base):
    __tablename__ = "books"

    id_book: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer)

    id_author: Mapped[int] = mapped_column(
        ForeignKey("authors.id_author"),
        nullable=False
    )

    author: Mapped["Author"] = relationship(
        back_populates="books"
    )

    loans: Mapped[List["Loan"]] = relationship(
        back_populates="book",
        cascade="all, delete-orphan"
    )
