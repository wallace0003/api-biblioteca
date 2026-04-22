import requests

BASE_URL = "http://localhost:8000/api"


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get_users(self):
        return requests.get(f"{self.base_url}/users").json()

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}").json()

    def create_user(self, data):
        return requests.post(f"{self.base_url}/users", json=data).json()

    def update_user(self, user_id, data):
        return requests.put(f"{self.base_url}/users/{user_id}", json=data).json()

    def delete_user(self, user_id):
        return requests.delete(f"{self.base_url}/users/{user_id}").json()

    def get_authors(self):
        return requests.get(f"{self.base_url}/authors").json()

    def create_author(self, data):
        return requests.post(f"{self.base_url}/authors", json=data).json()

    def get_author(self, author_id):
        return requests.get(f"{self.base_url}/authors/{author_id}").json()

    def update_author(self, author_id, data):
        return requests.put(f"{self.base_url}/authors/{author_id}", json=data).json()

    def delete_author(self, author_id):
        return requests.delete(f"{self.base_url}/authors/{author_id}").json()

    def get_books(self):
        return requests.get(f"{self.base_url}/books").json()

    def create_book(self, data):
        return requests.post(f"{self.base_url}/books", json=data).json()

    def get_book(self, book_id):
        return requests.get(f"{self.base_url}/books/{book_id}").json()

    def update_book(self, book_id, data):
        return requests.put(f"{self.base_url}/books/{book_id}", json=data).json()

    def delete_book(self, book_id):
        return requests.delete(f"{self.base_url}/books/{book_id}").json()

    def get_loans(self):
        return requests.get(f"{self.base_url}/loans").json()

    def create_loan(self, data):
        return requests.post(f"{self.base_url}/loans", json=data).json()

    def get_loan(self, loan_id):
        return requests.get(f"{self.base_url}/loans/{loan_id}").json()

    def update_loan(self, loan_id, data):
        return requests.put(f"{self.base_url}/loans/{loan_id}", json=data).json()

    def delete_loan(self, loan_id):
        return requests.delete(f"{self.base_url}/loans/{loan_id}").json()

    def get_logs(self):
        return requests.get(f"{self.base_url}/logs").json()

    def get_log(self, log_id):
        return requests.get(f"{self.base_url}/logs/{log_id}").json()

    def delete_log(self, log_id):
        return requests.delete(f"{self.base_url}/logs/{log_id}").json()

    def clear_logs(self):
        return requests.delete(f"{self.base_url}/logs").json()

    def generate_logs(self):
        return requests.post(f"{self.base_url}/logs/generate").json()