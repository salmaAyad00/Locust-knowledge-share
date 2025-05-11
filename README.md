# Locust Load Testing - TaskSet, Nested TaskSet, and Sequential TaskSet Guide

This document serves as a guide for using **TaskSet**, **Nested TaskSet**, and **Sequential TaskSet** in Locust. These concepts allow you to model complex user behaviors by grouping related tasks and controlling their flow. Understanding how to structure these task sets will enable you to create more realistic and efficient load tests.

## 1. **TaskSet**

### Definition:
In Locust, a **`TaskSet`** is a container for a group of related tasks that a simulated user will execute. Tasks within a `TaskSet` are defined as methods, and each method can represent an individual action the user would take, such as making an HTTP request.

A **`TaskSet`** can be attached to a `User` class, and it allows you to simulate sequences of actions that a user performs in a session.

### Built-in Methods:
- **`task()`**: The decorator used to mark methods within a `TaskSet` as tasks. These tasks will be executed when the user is simulated.
- **`self.client.get()`**: Performs an HTTP GET request as part of the task.
- **`self.client.post()`**: Performs an HTTP POST request.
- **`self.client.put()`**: Performs an HTTP PUT request.
- **`self.client.delete()`**: Performs an HTTP DELETE request.

### Use Case:
- **Basic User Actions**: You would use a `TaskSet` when simulating a series of user actions such as logging in, viewing a product, and checking out.

---

## 2. **Nested TaskSet**

### Definition:
A **Nested TaskSet** refers to embedding one TaskSet within another. This allows you to model more complex user behaviors by creating sub-sequences of tasks that can be reused within different contexts.

Nested task sets are useful when you need to simulate a flow that depends on performing a set of actions first (e.g., authentication) before proceeding to other actions.

### Differences from TaskSet:
- **Composition**: Nested TaskSets allow you to build more modular and reusable task sequences by including one TaskSet inside another.
- **Hierarchy**: They introduce a hierarchical structure, where each parent TaskSet can call upon one or more nested TaskSets.

### Built-in Methods:
- **tasks**: In a parent TaskSet, the `tasks` attribute can be set to reference another TaskSet class or a list of tasks. This provides the ability to nest task sets.

### Use Case:
- **Authentication Flows**: For example, you could create an authentication TaskSet and nest it within a UserActions task set, ensuring that each user first logs in before proceeding to other actions.

---

## 3. **Sequential TaskSet**

### Definition:
A **Sequential TaskSet** ensures that tasks within a TaskSet are executed in a specific, ordered sequence. This is useful when actions depend on the results or completion of previous steps, mimicking a real user journey.

In a Sequential TaskSet, the tasks will always be executed in the defined order, one after the other.

### Differences from TaskSet:
- **Order of Execution**: While tasks in a basic TaskSet can be executed in any order, sequential task execution ensures that the order of tasks matters.
- **Control over Workflow**: Sequential task sets are useful when you need to model a user’s step-by-step journey through an application.

### Built-in Methods:
- **task()**: The decorator used to mark methods as tasks, with an implicit sequential order based on the order of definition in the class.
- **wait_time**: Can be used to define the wait time between sequential tasks, creating pauses between steps.

### Use Case:
- **Login to Logout Flow**: In scenarios where a user must log in, view their profile, and then log out, you would use a Sequential TaskSet to model this flow.

---

## Conclusion

Understanding and utilizing **TaskSet**, **Nested TaskSet**, and **Sequential TaskSet** in Locust allows you to design more sophisticated load tests that simulate realistic user behavior and interactions. 
By combining these elements effectively, you can model complex user journeys and ensure your application can handle different types of usage scenarios.