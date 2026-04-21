from sqlalchemy.orm import Session
from app.models import Loan
from app.schemas.loan import LoanCreate, LoanUpdate
from datetime import datetime, UTC
from app.db.mongo.mongo_client import MongoClientManager


class LoanService:
    def __init__(self, mongo: MongoClientManager):
        self.mongo = mongo

    def _to_dict_list(self, loans):
        return [
            {
                "id_loan": l.id_loan,
                "id_user": l.id_user,
                "id_book": l.id_book,
                "created_at": l.created_at.isoformat() if l.created_at else None,
                "date_loan": l.date_loan.isoformat() if l.date_loan else None,
                "date_return": l.date_return.isoformat() if l.date_return else None,
                "date_expected_return": 
                    l.date_expected_return.isoformat() if l.date_expected_return else None
            }
            for l in loans
        ]

    def create(self, db: Session, data: LoanCreate):
        loan = Loan(
            **data.model_dump(),
            created_at=datetime.now(UTC)
        )

        db.add(loan)
        db.commit()
        db.refresh(loan)

        try:
            self.mongo.insert_log("logs", {
                "event": "CREATE_LOAN",
                "loan_id": loan.id_loan,
                "data": data.model_dump()
            })
        except:
            pass

        return loan

    def get_all(self, db: Session):
        loans = db.query(Loan).all()

        print("🐢 PostgreSQL HIT")

        try:
            self.mongo.insert_log("logs", {
                "event": "GET_ALL_LOANS",
                "source": "database",
                "count": len(loans)
            })
        except:
            pass

        return loans

    def get_by_id(self, db: Session, id_loan: int):
        loan = db.query(Loan).filter(Loan.id_loan == id_loan).first()

        try:
            self.mongo.insert_log("logs", {
                "event": "GET_LOAN",
                "loan_id": id_loan,
                "found": bool(loan)
            })
        except:
            pass

        return loan

    def update(self, db: Session, id_loan: int, data: LoanUpdate):
        loan = db.query(Loan).filter(Loan.id_loan == id_loan).first()

        if not loan:
            try:
                self.mongo.insert_log("logs", {
                    "event": "UPDATE_LOAN",
                    "loan_id": id_loan,
                    "status": "NOT_FOUND"
                })
            except:
                pass
            return None

        old_data = {
            "date_loan": loan.date_loan,
            "date_return": loan.date_return,
            "date_expected_return": loan.date_expected_return
        }

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(loan, key, value)

        db.commit()
        db.refresh(loan)

        try:
            self.mongo.insert_log("logs", {
                "event": "UPDATE_LOAN",
                "loan_id": id_loan,
                "old_data": old_data,
                "new_data": data.model_dump(exclude_unset=True)
            })
        except:
            pass

        return loan

    def delete(self, db: Session, id_loan: int):
        loan = db.query(Loan).filter(Loan.id_loan == id_loan).first()

        if not loan:
            try:
                self.mongo.insert_log("logs", {
                    "event": "DELETE_LOAN",
                    "loan_id": id_loan,
                    "status": "NOT_FOUND"
                })
            except:
                pass
            return False

        db.delete(loan)
        db.commit()

        try:
            self.mongo.insert_log("logs", {
                "event": "DELETE_LOAN",
                "loan_id": id_loan,
                "status": "SUCCESS"
            })
        except:
            pass

        return True