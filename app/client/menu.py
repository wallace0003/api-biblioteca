from pprint import pprint
from app.client.endpoints import APIClient


client = APIClient()


def pause():
    input("\nPressione ENTER para continuar...")


def read_int(label):
    while True:
        try:
            return int(input(label))
        except ValueError:
            print("Digite um número válido.")


def menu_users():
    while True:
        print("\n=== USUÁRIOS ===")
        print("1 - Listar usuários")
        print("2 - Buscar usuário por ID")
        print("3 - Criar usuário")
        print("4 - Atualizar usuário")
        print("5 - Deletar usuário")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            pprint(client.get_users())

        elif opcao == "2":
            user_id = read_int("ID do usuário: ")
            pprint(client.get_user_by_id(user_id))

        elif opcao == "3":
            data = {
                "user_name": input("Nome: "),
                "email": input("Email: "),
            }
            pprint(client.create_user(data))

        elif opcao == "4":
            user_id = read_int("ID do usuário: ")
            data = {}

            user_name = input("Novo nome, ou ENTER para manter: ")
            email = input("Novo email, ou ENTER para manter: ")

            if user_name:
                data["user_name"] = user_name
            if email:
                data["email"] = email

            pprint(client.update_user(user_id, data))

        elif opcao == "5":
            user_id = read_int("ID do usuário: ")
            pprint(client.delete_user(user_id))

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

        pause()


def menu_authors():
    while True:
        print("\n=== AUTORES ===")
        print("1 - Listar autores")
        print("2 - Buscar autor por ID")
        print("3 - Criar autor")
        print("4 - Atualizar autor")
        print("5 - Deletar autor")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            pprint(client.get_authors())

        elif opcao == "2":
            author_id = read_int("ID do autor: ")
            pprint(client.get_author(author_id))

        elif opcao == "3":
            data = {
                "author_name": input("Nome do autor: "),
            }
            pprint(client.create_author(data))

        elif opcao == "4":
            author_id = read_int("ID do autor: ")
            data = {
                "author_name": input("Novo nome do autor: "),
            }
            pprint(client.update_author(author_id, data))

        elif opcao == "5":
            author_id = read_int("ID do autor: ")
            pprint(client.delete_author(author_id))

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

        pause()


def menu_books():
    while True:
        print("\n=== LIVROS ===")
        print("1 - Listar livros")
        print("2 - Buscar livro por ID")
        print("3 - Criar livro")
        print("4 - Atualizar livro")
        print("5 - Deletar livro")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            pprint(client.get_books())

        elif opcao == "2":
            book_id = read_int("ID do livro: ")
            pprint(client.get_book(book_id))

        elif opcao == "3":
            data = {
                "title": input("Título: "),
                "id_author": read_int("ID do autor: "),
                "year": read_int("Ano de lançamento: ")
            }
            pprint(client.create_book(data))

        elif opcao == "4":
            book_id = read_int("ID do livro: ")
            data = {}

            title = input("Novo título, ou ENTER para manter: ")
            author_id = input("Novo ID do autor, ou ENTER para manter: ")

            if title:
                data["title"] = title
            if author_id:
                data["id_author"] = int(author_id)

            pprint(client.update_book(book_id, data))

        elif opcao == "5":
            book_id = read_int("ID do livro: ")
            pprint(client.delete_book(book_id))

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

        pause()


def menu_loans():
    while True:
        print("\n=== EMPRÉSTIMOS ===")
        print("1 - Listar empréstimos")
        print("2 - Buscar empréstimo por ID")
        print("3 - Criar empréstimo")
        print("4 - Atualizar empréstimo")
        print("5 - Deletar empréstimo")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            pprint(client.get_loans())

        elif opcao == "2":
            loan_id = read_int("ID do empréstimo: ")
            pprint(client.get_loan(loan_id))

        elif opcao == "3":
            data = {
                "id_user": read_int("ID do usuário: "),
                "id_book": read_int("ID do livro: "),
                "date_expected_return": input("Data devolução:")
            }
            pprint(client.create_loan(data))

        elif opcao == "4":
            loan_id = read_int("ID do empréstimo: ")
            data = {}

            user_id = input("Novo ID do usuário, ou ENTER para manter: ")
            book_id = input("Novo ID do livro, ou ENTER para manter: ")

            if user_id:
                data["id_user"] = int(user_id)
            if book_id:
                data["id_book"] = int(book_id)

            pprint(client.update_loan(loan_id, data))

        elif opcao == "5":
            loan_id = read_int("ID do empréstimo: ")
            pprint(client.delete_loan(loan_id))

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

        pause()


def menu_logs():
    while True:
        print("\n=== LOGS ===")
        print("1 - Listar logs")
        print("2 - Buscar log por ID")
        print("3 - Buscar logs por evento")
        print("4 - Deletar log")
        print("5 - Limpar todos os logs")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            pprint(client.get_logs())

        elif opcao == "2":
            log_id = input("ID do log: ")
            pprint(client.get_log(log_id))

        elif opcao == "3":
            event = input("Evento: ")
            pprint(client.get_logs_by_event(event))

        elif opcao == "4":
            log_id = input("ID do log: ")
            pprint(client.delete_log(log_id))

        elif opcao == "5":
            confirm = input("Tem certeza? Digite SIM: ")
            if confirm == "SIM":
                pprint(client.clear_logs())
            else:
                print("Operação cancelada.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

        pause()


def menu():
    while True:
        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Usuários")
        print("2 - Autores")
        print("3 - Livros")
        print("4 - Empréstimos")
        print("5 - Logs")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            menu_users()

        elif opcao == "2":
            menu_authors()

        elif opcao == "3":
            menu_books()

        elif opcao == "4":
            menu_loans()

        elif opcao == "5":
            menu_logs()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
