from locust import TaskSet, constant, task, HttpUser
from requests import RequestException


class UserLogin(TaskSet):
    @task
    def login(self):
        res=self.client.post("/auth/login/", 
                             json={"email": "salma.ayad+password@flextock.com", "password": "Omar@1234"})
        print(f"Response of login: {res.status_code}")


class ListOutboundOrder(TaskSet):
            
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
 
    @task        
    class UpdateOutboundOrderStatus(TaskSet):
    
        @task    
        def update_order_status(self):
            try:
                res=self.client.post("/orders/outbounds/e9cda005-31c1-44a6-a8c2-247d938b5cdb/update_status", headers=
                            {
                    "Authorization":
                        "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ2OTQ3MDc0LCJpYXQiOjE3NDY5NDMxODgsImp0aSI6IjhmN2EyZTE1MTFhMjQ0ZmFhYzJiYzBiMzA0Y2IzYjNmIiwidXNlcl9pZCI6MTIxLCJlbWFpbCI6InNhbG1hLmF5YWQrcGFzc3dvcmRAZmxleHRvY2suY29tIiwibmFtZSI6InBhc3N3b3JkLWNoZWNrIiwic3RhZmYiOnRydWUsImlzX21hc3Rlcl91c2VyIjpmYWxzZSwiaXNfZW1haWxfdmVyaWZpZWQiOnRydWUsInBlcm1pc3Npb25zIjpbXX0.Sks4t1sWCEHlDMAdSy8kaMhcWnzulRnHk45EZ4m_mXg"
                    },
                        json={'status': "pending"}
                    )
                print(f"Response of update order status: {res.status_code}")
                # to make handle goes to the parent class
                self.interrupt(reschedule=False)
            except RequestException as e:
                print(f"Update status Request failed: {e}")         
    
            
    
class UpdateOrderStatus(HttpUser):
        wait_time=constant(1)
        host= "https://core-stg-rkcv4cncjq-uc.a.run.app"    
        tasks=[ListOutboundOrder]
        
         
             
    