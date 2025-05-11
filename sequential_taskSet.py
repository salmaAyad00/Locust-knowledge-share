from locust import SequentialTaskSet, constant, task, HttpUser
from requests import RequestException


class ListOutboundOrders(SequentialTaskSet):
            
    @task
    def get_orders(self):
        try:
            res=self.client.get("/orders/outbounds", headers=
                            {
                    "Authorization":
                        "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ2OTQ3MDc0LCJpYXQiOjE3NDY5NDMxODgsImp0aSI6IjhmN2EyZTE1MTFhMjQ0ZmFhYzJiYzBiMzA0Y2IzYjNmIiwidXNlcl9pZCI6MTIxLCJlbWFpbCI6InNhbG1hLmF5YWQrcGFzc3dvcmRAZmxleHRvY2suY29tIiwibmFtZSI6InBhc3N3b3JkLWNoZWNrIiwic3RhZmYiOnRydWUsImlzX21hc3Rlcl91c2VyIjpmYWxzZSwiaXNfZW1haWxfdmVyaWZpZWQiOnRydWUsInBlcm1pc3Npb25zIjpbXX0.Sks4t1sWCEHlDMAdSy8kaMhcWnzulRnHk45EZ4m_mXg"
                    })
            print(f"Response of get orders: {res.status_code}")
        except RequestException as e:
            print(f"Request failed: {e}")
            
            
    @task
    def get_order(self):
        try:
            res=self.client.get("/orders/outbounds/e9cda005-31c1-44a6-a8c2-247d938b5cdb", headers=
                            {
                    "Authorization":
                        "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ2OTQ3MDc0LCJpYXQiOjE3NDY5NDMxODgsImp0aSI6IjhmN2EyZTE1MTFhMjQ0ZmFhYzJiYzBiMzA0Y2IzYjNmIiwidXNlcl9pZCI6MTIxLCJlbWFpbCI6InNhbG1hLmF5YWQrcGFzc3dvcmRAZmxleHRvY2suY29tIiwibmFtZSI6InBhc3N3b3JkLWNoZWNrIiwic3RhZmYiOnRydWUsImlzX21hc3Rlcl91c2VyIjpmYWxzZSwiaXNfZW1haWxfdmVyaWZpZWQiOnRydWUsInBlcm1pc3Npb25zIjpbXX0.Sks4t1sWCEHlDMAdSy8kaMhcWnzulRnHk45EZ4m_mXg"
                    })
            print(f"Response of get order: {res.status_code}")
        except RequestException as e:
            print(f"Request failed: {e}")
            
class ExcuterClass(HttpUser):
    wait_time=constant(1)
    host= "https://core-stg-rkcv4cncjq-uc.a.run.app"    
    tasks=[ListOutboundOrders]
    
                