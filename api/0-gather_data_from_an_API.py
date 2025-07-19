#!/usr/bin/python3
"""Fetches and displays TODO list progress for a given employee ID"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and print the TODO progress for an employee"""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data")
        return

    employee = user_response.json()
    todos = todos_response.json()

    employee_name = employee.get('name')
    total_tasks = len(todos)
    done_tasks = [
        task.get('title') for task in todos if task.get('completed')
    ]

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(done_tasks)}/{total_tasks}):"
    )
    for title in done_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
