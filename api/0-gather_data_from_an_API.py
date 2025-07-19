#!/usr/bin/python3
"""
This module fetches and displays the TODO list progress for a given employee
from the JSONPlaceholder REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and prints the TODO list progress for the specified employee.
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )

    user_response = requests.get(user_url)
    user = user_response.json()

    employee_name = user.get('name')
    if not employee_name:
        print("Employee not found.")
        return

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]
    done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({done_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_progress.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer employee ID.")
        sys.exit(1)
