# Stress Testing with Locust

## ✨ Key Concept

> "Load testing asks: can it handle 100 users?"
>
> "Stress testing asks: what happens when I throw 5000 at it?"

Stress testing is **not** about pass/fail. It is about **observation**: how your system behaves when pushed beyond its limits.

> Key takeaway: **1000 users ≠ 1000 requests/sec** — requests take time, users get blocked waiting
---

## 🔹 Stress Scenario

### Target Endpoint

- **Endpoint**: `POST /auth/login`
- **Payload**:
  ```json
  {
    "email": "user@example.com",
    "password": "SuperSecret"
  }
  ```

### Locust Settings

- `wait_time = between(0, 0)` → No delay between requests
- Start with **2 users** to get a baseline


> "We're going to overload the login endpoint and watch it struggle."

---

## 🔍 What to Observe: Locust UI Metrics

| Column                   | Meaning                                                 |
| ------------------------ | ------------------------------------------------------- |
| **Type**                 | HTTP method used (e.g. GET, POST)                       |
| **Name**                 | Endpoint name or URL                                    |
| **# Requests**           | Total number of requests completed (including failures) |
| **# Fails**              | Number of failed requests                               |
| **Median (ms)**          | 50% of requests completed faster than this time         |
| **95%ile (ms)**          | 95% of requests completed faster than this time         |
| **99%ile (ms)**          | 99% of requests completed faster than this time         |
| **Average (ms)**         | Average response time across all requests               |
| **Min / Max (ms)**       | Fastest and slowest request durations                   |
| **Average Size (bytes)** | Average response payload size                           |
| **Current RPS**          | Requests per second currently being handled             |
| **Current Failures/s**   | Failures occurring per second currently                 |

---

## 🔢 Live Test 

- Start with **2000 users** → show low latency and healthy response
- Scale to **2000 users with 2000 RPS**
- Observe:
  - RPS 
  -Backend resource usage (CPU, memory, DB)
---


