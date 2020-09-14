#!/usr/bin/python3
"""0x15 - 1"""
import csv
import requests
import sys


if __name__ == "__main__":
    tasks = []  # List of tasks
    eid = sys.argv[1]
    filename = "{}.csv".format(eid)
    reqname = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(eid)).json()
    enm = reqname.get('name')   # Employee Name
    todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(eid)).json()
    with open(filename, 'w') as csvf:
        writer = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([eid, enm,
                            task.get('completed'), task.get('title')])
