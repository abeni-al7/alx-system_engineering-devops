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
    print(users)
    data = {}
    for user in users:
        tasks = []
        todos = requests.get(url + "todos?userId={}".format(
            user.get("id"))).json()
        for todo in todos:
            tasks.append({"username": user.get("username"),
                          "task": todo.get("title"),
                          "completed": todo.get("completed")})
        data[user.get("id")] = tasks
        print(data)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
