#!/usr/bin/python3
"""Exports TODO list data for a given employee ID to CSV format"""

import csv
import requests
import sys


def export_employee_todos_to_csv(employee_id):
    """Fetch and export the TODO list of an employee to a CSV file"""
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

    username = employee.get('username')

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todos_to_csv(employee_id)
