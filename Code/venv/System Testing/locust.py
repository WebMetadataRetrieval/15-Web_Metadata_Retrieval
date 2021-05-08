from locust import HttpUser, task, TaskSet, between
class StressTesting(HttpUser):
    wait_time = between(5, 30)

    @task(1)
    def index_page(self):
        self.client.get(url="")

    @task(2)
    def register_page(self):
        response = self.client.get(url="register")
        csrftoken = response.cookies['csrftoken']
        response = self.client.post("register/", {"email": "test", "password": "secret"}, headers={"X-CSRFToken": csrftoken})

    @task(3)
    def login_page(self):
        response = self.client.get(url="login")
        csrftoken = response.cookies['csrftoken']
        response = self.client.post("login/", {"email": "test", "password": "secret"}, headers={"X-CSRFToken": csrftoken})


    @task(4)
    def account_page(self):
        self.client.get(url="account")

    @task(5)
    def api_page(self):
       
        api_key= "2bed2a0c-3d1f-4775-a45a-7ffdddb17622" 
        web_page= "https://www.youtube.com/watch?v=hnrQ_bTsNMQ"
        cached= "True"
        daily_limit= 100000

        self.client.get("api/?api_key="+api_key+"&web_page="+web_page+"&cached="+cached, name = "api")
    
    @task(6)
    def logout_page(self):
        self.client.get(url='logout')