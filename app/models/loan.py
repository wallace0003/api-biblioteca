from datetime import datetime
from sqlalchemy import Integer, ForeignKey, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.models.base import Base


class Loan(Base):
    __tablename__ = "loans"

    id_loan: Mapped[int] = mapped_column(Integer, primary_key=True)

    id_user: Mapped[int] = mapped_column(
        ForeignKey("users.id_user"),
        nullable=False
    )

    id_book: Mapped[int] = mapped_column(
        ForeignKey("books.id_book"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now()
    )

    date_loan: Mapped[datetime] = mapped_column(Date, nullable=False, default=datetime.now())
    date_return: Mapped[datetime] = mapped_column(Date, nullable=True)
    date_expected_return: Mapped[datetime] = mapped_column(Date, nullable=True)

    user: Mapped["User"] = relationship(
        back_populates="loans"
    )

    book: Mapped["Book"] = relationship(
        back_populates="loans"
    )
