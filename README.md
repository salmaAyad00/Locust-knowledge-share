# Locust: `on_start` and `on_stop` Guide

## Overview

Locust provides two special lifecycle methods for task execution:

- **`on_start()`**: Runs **once** when a simulated user starts.
- **`on_stop()`**: Runs **once** when the user stops or completes the task set.

These methods are commonly used for:
- Logging in/out users
- Initializing state or data
- Cleaning up after tasks

---

## Behavior in Different Task Types

### 🔁 TaskSet

- Tasks are **executed randomly** unless weighted.
- `on_start()` runs **before the first task**.
- `on_stop()` runs **after the user finishes or exits** the task set.
- Suitable for load testing endpoints with **non-sequential behavior**.

### ➡️ SequentialTaskSet

- Tasks are **executed in the defined order**, one after another.
- `on_start()` runs **before the first task** in the sequence.
- `on_stop()` runs **after the last task** in the sequence.
- Ideal for simulating **real user flows** (e.g., login → browse → purchase → logout).

---

## Summary Table

| Feature                  | TaskSet                         | SequentialTaskSet                  |
|--------------------------|----------------------------------|------------------------------------|
| Task Execution Order     | Random                          | Defined (sequential)               |
| `on_start()`             | Before any task                 | Before the first sequential task   |
| `on_stop()`              | After test/user ends            | After last task completes          |
| Use Case                 | Random API hits / Load testing  | End-to-end user scenario testing   |

---
