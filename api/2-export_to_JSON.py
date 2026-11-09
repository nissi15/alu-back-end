#!/usr/bin/python3
"""Export the TODO list of an employee to a JSON file using a REST API."""
import json
import requests
import sys

base = "https://jsonplaceholder.typicode.com"


def get_user(user_id):
    """Return the user with the given ID, or None if the request fails."""
    response = requests.get("{}/users/{}".format(base, user_id))

    if response.status_code == 200:
        return response.json()
    else:
        print("GET user failed:", response.status_code)
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
    user_id = sys.argv[1]
    user = get_user(user_id)
    todos = get_todos(user_id)

    if user is not None and todos is not None:
        tasks = []
        for task in todos:
            tasks.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            })

        with open("{}.json".format(user_id), "w") as json_file:
            json.dump({user_id: tasks}, json_file)
