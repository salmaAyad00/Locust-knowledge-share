# Locust-knowledge-share
# Locust Demo: Load Testing with Multiple User Classes

This project demonstrates how to create a simple load testing suite using [Locust](https://locust.io/). It includes three user classes that simulate different behaviors using various `wait_time` strategies and task sets.

## Files

- `init.py`: Contains the test classes and tasks used for simulating users.

## User Classes

- `MyFisrtTest`: Uses constant wait time between tasks (1 second).
- `MySecondTest`: Uses a random wait time between 2 to 5 seconds.
- `MyThirdTest`: Uses `constant_pacing(5)`, ensuring tasks are spaced exactly 5 seconds apart including task execution time.

Each class contains two task methods which simply print test messages.

## Run commands

```bash
locust -f init.py
```

#### Or

```bash
locust -f locustfile.py --headless -u 10 -r 2 --run-time 1m
```

In Locust, headless mode means running the load test without the web interface

-u 10: Simulates 10 users
-r 2: Spawns 2 users per second,  --spawn-rate: How many users are created (spawned) per second
--run-time 1m: Runs the test for 1 minute


