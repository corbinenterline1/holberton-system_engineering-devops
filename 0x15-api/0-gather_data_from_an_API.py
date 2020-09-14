#!/usr/bin/python3
"""0x15 - 0"""
import json
import requests
import sys


if __name__ == "__main__":
    tasksdone = []  # List of tasks completed
    reqname = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(sys.argv[1])).json()
    enm = reqname.get('name')   # Employee Name
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(sys.argv[1])).json()
    taskcnt = len(todos)  # Total number of tasks
    tasksdonecnt = 0
    for task in todos:
        if task.get('completed') is True:
            tasksdone.append(task)
            tasksdonecnt += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(enm, tasksdonecnt, taskcnt))
    for task in tasksdone:
        print("\t {}".format(task.get('title')))
