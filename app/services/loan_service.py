# app/services/loan_service.py

from sqlalchemy.orm import Session
from app.models import Loan
from app.schemas.loan import LoanCreate, LoanUpdate
from datetime import datetime

class LoanService:

    @staticmethod
    def create(db: Session, data: LoanCreate):
        loan = Loan(
            **data.model_dump(),
            created_at=datetime.utcnow()
        )

        db.add(loan)
        db.commit()
        db.refresh(loan)
        return loan

    @staticmethod
    def get_all(db: Session):
        return db.query(Loan).all()

    @staticmethod
    def get_by_id(db: Session, id_loan: int):
        return db.query(Loan).filter(Loan.id_loan == id_loan).first()

    @staticmethod
    def update(db: Session, id_loan: int, data: LoanUpdate):
        loan = db.query(Loan).filter(Loan.id_loan == id_loan).first()

        if not loan:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(loan, key, value)

        db.commit()
        db.refresh(loan)
        return loan

    @staticmethod
    def delete(db: Session, id_loan: int):
        loan = db.query(Loan).filter(Loan.id_loan == id_loan).first()

        if not loan:
            return False

        db.delete(loan)
        db.commit()
        return True
