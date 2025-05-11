import time
from locust import User, constant, constant_pacing, task, between

class MyFisrtTest(User):
    weight= 2
    wait_time = constant(1)
    
    @task
    def my_first_test(self):
        print("Hello World, this is my first test")
    
    @task
    def my_second_test(self):
        print("Hello World, this is my second test")
        

class MySecondTest(User):
    weight=2
    wait_time = between(2, 5)
    
    @task
    def launch_test(self):
        print("Hello from the second test class.... launch_test 2")
        
    @task
    def search_test(self):
        print("Hello from the second test class.... search_test 2")
       
       
        
class MyThirdTest(User):
    weight=2
    wait_time = constant_pacing(5) 
       
    @task
    def launch_test(self):
        time.sleep(2)
        print("Hello from the third test class.... launch_test 3")
        
    @task
    def search_test(self):
        time.sleep(5)
        print("Hello from the third test class.... search_test 3")
        
    