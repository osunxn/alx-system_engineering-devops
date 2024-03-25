#!/usr/bin/python3
"""
Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    # Fetching employee data
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    # Fetching TODO list
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = requests.get(url)
    todos = response.json()

    # Processing TODO list
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    total_done_tasks = len(done_tasks)

    # Displaying the information
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, total_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
