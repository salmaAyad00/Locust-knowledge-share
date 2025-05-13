from locust import HttpUser, constant, task
from requests import RequestException       


class HttpcoreUser(HttpUser):
    wait_time=constant(1)
    host= "https://core-stg-rkcv4cncjq-uc.a.run.app"
    
    @task
    def login(self):
        res=self.client.post("/auth/login/", 
                             json={"email": "salma.ayad+password@flextock.com", "password": "Omar@1234"})
        print(f"Response of login: {res.status_code}")
    
    @task
    def get_orders(self):
        try:
            res=self.client.get("/orders/outbounds/?sort[]=-created_at&page=1&per_page=100", headers=
                            {
                    "Authorization":
                        "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ2OTQ3MDc0LCJpYXQiOjE3NDY5NDMxODgsImp0aSI6IjhmN2EyZTE1MTFhMjQ0ZmFhYzJiYzBiMzA0Y2IzYjNmIiwidXNlcl9pZCI6MTIxLCJlbWFpbCI6InNhbG1hLmF5YWQrcGFzc3dvcmRAZmxleHRvY2suY29tIiwibmFtZSI6InBhc3N3b3JkLWNoZWNrIiwic3RhZmYiOnRydWUsImlzX21hc3Rlcl91c2VyIjpmYWxzZSwiaXNfZW1haWxfdmVyaWZpZWQiOnRydWUsInBlcm1pc3Npb25zIjpbXX0.Sks4t1sWCEHlDMAdSy8kaMhcWnzulRnHk45EZ4m_mXg"
                    })
            print(f"Response of list orders: {res.status_code}")
        except RequestException as e:
            print(f"Request failed: {e}")    
    
    
        
        
        