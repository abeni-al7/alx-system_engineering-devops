#!/usr/bin/python3
"""This script uses a REST API to get information about a given employee ID
and returns information about his/her TODO list progress.
It then exports the data in the JSON format. recording all tasks from
all employees to a file named todo_all_employees.json."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    data = {}
    for user in users:
        tasks = []
        for todo in todos:
            if todo.get("userId") == user.get("id"):
                tasks.append({"task": todo.get("title"),
                              "completed": todo.get("completed"),
                              "username": user.get("username")})
        data[user.get("id")] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
