from datetime import datetime
from sqlalchemy import Integer, DateTime, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Loan(Base):
    __tablename__ = "loan"

    id_loan: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_user: Mapped[int] = mapped_column(
        ForeignKey("user.user_id"),
        nullable=False
    )
    id_book: Mapped[int] = mapped_column(
        ForeignKey("book.id_book"),
        nullable=False
    )
    date_loan: Mapped[datetime] = mapped_column(Date, nullable=False)
    date_return: Mapped[datetime] = mapped_column(Date, nullable=True)
    date_expected_return: Mapped[datetime] = mapped_column(Date, nullable=False)

    user: Mapped["User"] = relationship(
        back_populates="loans"
    )

    book: Mapped["Book"] = relationship(
        back_populates="loans"
    )
