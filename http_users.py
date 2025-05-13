from locust import HttpUser, constant, task

class HttpUsersTest(HttpUser):
    wait_time=constant(1)
    host= "https://reqres.in/api"
    
    @task
    def get_users(self):
        res=self.client.get("/users?page=2")
        print(f"Response of get user: {res.status_code}")
        
    @task
    def create_user(self):
        res=self.client.post("/users", json={"name": "morpheus", "job": "leader"})
        print(f"Response of create user: {res.status_code}")
        
 