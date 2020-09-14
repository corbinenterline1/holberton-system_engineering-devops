#!/usr/bin/python3
"""0x15 - 3"""
import json
import requests
import sys


if __name__ == "__main__":
    taskdic = {}    # Final form for file writing
    tasks = []  # List of tasks
    filename = "todo_all_employees.json"
    users = requests.get(
            "https://jsonplaceholder.typicode.com/users").json()
    for user in users:
        eid = user.get('id')
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(eid)).json()
        unm = user.get('username')
        todos = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}"
                .format(eid)).json()
        for task in todos:
            frmobj = {}     # formatted object
            frmobj['task'] = task.get('title')
            frmobj['completed'] = task.get('completed')
            frmobj['username'] = unm
            tasks.append(frmobj)
        taskdic[eid] = tasks
        with open(filename, 'w') as jsonf:
            json.dump(taskdic, jsonf)
