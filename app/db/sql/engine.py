from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import Base

class PostgresEngine():
    def __init__(self, database_url: str):
        self.database_url = database_url
        self._engine = None
        self._SessionLocal = None

    def create_engine(self) -> Engine:
        if not self._engine:
            self._engine = create_engine(
                url=self.database_url,
                echo=False,
                future=True
            )
        return self._engine

    def get_session(self) -> Session:
        if not self._SessionLocal:
            self._SessionLocal = sessionmaker(
                bind=self.create_engine(),
                autoflush=False,
                autocommit=False
            )
        return self._SessionLocal() 
    


if __name__ == "__main__":
    from datetime import date
    from app.models import User, Author, Book, Loan
    from app.db.sql.engine import PostgresEngine
    import os
    from dotenv import load_dotenv
    load_dotenv()

    def run_test():
        database_url = os.getenv("database_url")

        db = PostgresEngine(database_url=database_url).get_session()

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
    
    run_test()
