from locust import HttpUser, task
from order_data import ORDER_DATA
import threading

class OrderUser(HttpUser):
    url="http://127.0.0.1:8000/base/sync-shopify-orders/"
    
    @task
    def send_simultaneous_requests(self):
        """Send two requests simultaneously using threading."""
        
        def send_request():
            self.client.post(self.url, json=ORDER_DATA)
        
        # Create two threads to send requests at the same time
        thread1 = threading.Thread(target=send_request)
        thread2 = threading.Thread(target=send_request)
        
        # Start both threads at the same time
        thread1.start()
        thread2.start()
        
        # Wait for both threads to complete
        thread1.join()
        thread2.join()