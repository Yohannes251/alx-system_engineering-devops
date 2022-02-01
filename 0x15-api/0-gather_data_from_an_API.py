#!/usr/bin/python3
"""
    This script returns information about TODO list by using employee ID
"""

import requests
import sys


if __name__ == "__main__":
    completed_tasks = 0
    total_tasks = 0
    id = {'id': sys.argv[1]}
    uid = {'userId': sys.argv[1]}
    name = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=id).json()
    emp_name = name[0].get('name')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params=uid).json()
    for task in tasks:
        if (task.get('completed') is True):
            completed_tasks += 1
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(emp_name,
          completed_tasks, total_tasks))

    for task in tasks:
        if (task.get('completed') is True):
            print("\t {}".format(task.get('title')))
