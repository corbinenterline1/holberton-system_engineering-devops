#!/usr/bin/python3
"""0x15 - 2"""
import json
import requests
import sys


if __name__ == "__main__":
    taskdic = {}    # Final form for file writing
    tasks = []  # List of tasks
    eid = sys.argv[1]
    filename = "{}.csv".format(eid)
    reqname = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(eid)).json()
    unm = reqname.get('username')   # Employee Name
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
