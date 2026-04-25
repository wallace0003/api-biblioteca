import requests

BASE_URL = "http://localhost:8000/api/v1"


class APIClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url.rstrip("/")

    def _request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.request(method, url, json=data)
            response.raise_for_status()

            if response.content:
                return response.json()

            return {"message": "Operação realizada com sucesso"}

        except requests.exceptions.HTTPError:
            try:
                return response.json()
            except Exception:
                return {"error": response.text}

        except requests.exceptions.ConnectionError:
            return {"error": "Não foi possível conectar à API. Verifique se o FastAPI está rodando."}

    # Users
    def get_users(self):
        return self._request("GET", "/users/")

    def get_user_by_id(self, user_id):
        return self._request("GET", f"/users/{user_id}")

    def create_user(self, data):
        return self._request("POST", "/users/", data)

    def update_user(self, user_id, data):
        return self._request("PUT", f"/users/{user_id}", data)

    def delete_user(self, user_id):
        return self._request("DELETE", f"/users/{user_id}")

    # Authors
    def get_authors(self):
        return self._request("GET", "/authors/")

    def get_author(self, author_id):
        return self._request("GET", f"/authors/{author_id}")

    def create_author(self, data):
        return self._request("POST", "/authors/", data)

    def update_author(self, author_id, data):
        return self._request("PUT", f"/authors/{author_id}", data)

    def delete_author(self, author_id):
        return self._request("DELETE", f"/authors/{author_id}")

    # Books
    def get_books(self):
        return self._request("GET", "/books/")

    def get_book(self, book_id):
        return self._request("GET", f"/books/{book_id}")

    def create_book(self, data):
        return self._request("POST", "/books/", data)

    def update_book(self, book_id, data):
        return self._request("PUT", f"/books/{book_id}", data)

    def delete_book(self, book_id):
        return self._request("DELETE", f"/books/{book_id}")

    # Loans
    def get_loans(self):
        return self._request("GET", "/loans/")

    def get_loan(self, loan_id):
        return self._request("GET", f"/loans/{loan_id}")

    def create_loan(self, data):
        return self._request("POST", "/loans/", data)

    def update_loan(self, loan_id, data):
        return self._request("PUT", f"/loans/{loan_id}", data)

    def delete_loan(self, loan_id):
        return self._request("DELETE", f"/loans/{loan_id}")

    # Logs
    def get_logs(self):
        return self._request("GET", "/logs/")

    def get_log(self, log_id):
        return self._request("GET", f"/logs/{log_id}")

    def get_logs_by_event(self, event):
        return self._request("GET", f"/logs/event/{event}")

    def delete_log(self, log_id):
        return self._request("DELETE", f"/logs/{log_id}")

    def clear_logs(self):
        return self._request("DELETE", "/logs/")
