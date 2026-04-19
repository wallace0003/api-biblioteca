from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class LoanCreate(BaseModel):
    id_user: int
    id_book: int
    date_expected_return: date

class LoanUpdate(BaseModel):
    date_return: Optional[date] = None

class LoanResponse(BaseModel):
    id_loan: int
    id_user: int
    id_book: int
    created_at: datetime
    date_loan: date
    date_return: Optional[date]
    date_expected_return: date

    class Config:
        from_attributes = True
