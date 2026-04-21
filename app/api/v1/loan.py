from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.loan import LoanCreate, LoanResponse, LoanUpdate
from app.services.loan_service import LoanService
from app.api.dependecies import get_db, get_mongo

router = APIRouter()

@router.post("/", response_model=LoanResponse)
def create_loan(data: LoanCreate, db: Session = Depends(get_db)):
    return LoanService(get_mongo).create(db, data)

@router.get("/", response_model=list[LoanResponse])
def get_loans(db: Session = Depends(get_db)):
    return LoanService(get_mongo).get_all(db)

@router.get("/{id_loan}", response_model=LoanResponse)
def get_loan(id_loan: int, db: Session = Depends(get_db)):
    loan = LoanService(get_mongo).get_by_id(db, id_loan)

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    return loan

@router.put("/{id_loan}", response_model=LoanResponse)
def update_loan(id_loan: int, data: LoanUpdate, db: Session = Depends(get_db)):
    loan = LoanService(get_mongo).update(db, id_loan, data)

    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")

    return loan

@router.delete("/{id_loan}")
def delete_loan(id_loan: int, db: Session = Depends(get_db)):
    success = LoanService(get_mongo).delete(db, id_loan)

    if not success:
        raise HTTPException(status_code=404, detail="Loan not found")

    return {"message": "Loan deleted successfully"}
