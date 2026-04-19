from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv(
    "database_url", 
    "postgresql+psycopg2://admin:admin@localhost:5432/mydb"
)

engine = create_engine(
    DATABASE_URL,
    echo=False, 
    future=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

from datetime import date
from app.db.sql.engine import SessionLocal
from app.models import User, Author, Book, Loan


def run_test():
    db = SessionLocal()

    try:
        user = User(
            user_name="Wallace",
            email="wallace@email.com"
        )

        author = Author(
            author_name="George Orwell"
        )

        # 🔥 3. Criar livro
        book = Book(
            title="1984",
            year=1949,
            author=author  
        )

        loan = Loan(
            user=user,
            book=book,
            date_loan=date.today(),
            date_expected_return=date.today()
        )

        #db.add(loan)
        #db.commit()

        print("✅ Dados inseridos com sucesso!")

        loans = db.query(Loan).all()

        for l in loans:
            print(f"""
                📚 Livro: {l.book.title}
                👤 Usuário: {l.user.user_name}
                ✍️ Autor: {l.book.author.author_name}
                📅 Empréstimo: {l.date_loan}
            """)

    except Exception as e:
        db.rollback()
        print("❌ Erro:", e)

    finally:
        db.close()


if __name__ == "__main__":
    run_test()
