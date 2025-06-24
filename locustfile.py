from locust import HttpUser, task, between

class LoginStressUser(HttpUser):
    wait_time = between(0, 0)  # max stress

    @task
    def login(self):
        email = f"fawzy@example.com"
        password = "Fawzy@Fawzy"  # replace with realistic test password

        payload = {
            "email": email,
            "password": password
        }

        with self.client.post("/auth/login/", json=payload, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Login failed: {response.status_code}")

#locust -f locustfile.py --host https://core-dev-rkcv4cncjq-uc.a.run.app