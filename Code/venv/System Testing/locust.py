from locust import HttpUser, task, TaskSet, between
import time
from json import JSONDecodeError


class StressTesting(HttpUser):
    wait_time = between(1, 5)

    @task
    def index_page(self):
        self.client.get(url="")

    @task
    def register_page(self):
        response = self.client.get(url="register")
        csrftoken = response.cookies['csrftoken']
        response = self.client.post("register/", {"email": "test", "password": "secret"}, headers={"X-CSRFToken": csrftoken})

    @task
    def login_page(self):
        response = self.client.get(url="login")
        csrftoken = response.cookies['csrftoken']
        response = self.client.post("login/", {"email": "test", "password": "secret"}, headers={"X-CSRFToken": csrftoken})


    @task
    def account_page(self):
        self.client.get(url="account")

    # @task
    # def api_page(self):
    #     with self.client.post("api", json={"web_page": "https://test.com", "title": "random title", "description": "some long discription", "thumbnail": "https://thumbnail.png"}, catch_response=True) as response:
    #         try:
    #             if response.json()["title"] != "random title":
    #                 response.failure("Did not get expected value in greeting")
    #         except JSONDecodeError:
    #             response.failure("Response could not be decoded as JSON")
    #         except KeyError:
    #             response.failure("Response did not contain expected key 'greeting'")

    @task
    def logout_page(self):
        self.client.get(url='logout')