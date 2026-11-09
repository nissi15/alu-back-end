#!/usr/bin/python3
"""Export the TODO lists of all employees to a JSON file using a REST API."""
import json
import requests

base = "https://jsonplaceholder.typicode.com"


def get_users():
    """Return the list of all users, or None if the request fails."""
    response = requests.get("{}/users".format(base))

    if response.status_code == 200:
        return response.json()
    else:
        print("GET users failed:", response.status_code)
        return None


def get_todos(user_id):
    """Return the list of todos for the given user, or None on failure."""
    response = requests.get("{}/todos?userId={}".format(base, user_id))

    if response.status_code == 200:
        return response.json()
    else:
        print("GET todos failed:", response.status_code)
        return None


if __name__ == "__main__":
    users = get_users()

    if users is not None:
        all_tasks = {}
        for user in users:
            user_id = user.get("id")
            todos = get_todos(user_id)
            if todos is None:
                continue

            tasks = []
            for task in todos:
                tasks.append({
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
            all_tasks[str(user_id)] = tasks

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(all_tasks, json_file)
