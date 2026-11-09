#!/usr/bin/python3
"""Display the TODO list progress of an employee using a REST API."""
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
        done = []
        for task in todos:
            if task.get("completed"):
                done.append(task)

        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(done), len(todos)))
        for task in done:
            print("\t {}".format(task.get("title")))
