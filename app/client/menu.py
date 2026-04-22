from app.client.endpoints import APIClient

def menu():
    client = APIClient()

    while True:
        print("\n=== MENU ===")
        print("1 - Listar usuários")
        print("2 - Criar usuário")
        print("3 - Listar livros")
        print("4 - Criar livro")
        print("5 - Listar empréstimos")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print(client.get_users())

        elif opcao == "2":
            nome = input("Nome: ")
            email = input("Email: ")
            data = {"name": nome, "email": email}
            print(client.create_user(data))

        elif opcao == "3":
            print(client.get_books())

        elif opcao == "4":
            titulo = input("Título: ")
            author_id = int(input("Author ID: "))
            data = {"title": titulo, "author_id": author_id}
            print(client.create_book(data))

        elif opcao == "5":
            print(client.get_loans())

        elif opcao == "6":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()