# HttpUsersTest - Locust Load Test for User API

This file contains a basic Locust load test to simulate HTTP requests to the ReqRes API for user-related actions.

## Description

`http_users.py` defines a Locust `HttpUser` class that performs two types of HTTP requests:

1. **GET /users?page=2**: Fetches a list of users from page 2.
2. **POST /users**: Creates a new user with specified name and job attributes.

Each task will print the HTTP status code received in the response.

### core example on login, list outbound orders

