 #!/usr/bin/python3
import sys
import requests

def get_employee_todo_progress(employee_id):
    # Get user info
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Employee not found.")
        return

    user = response.json()
    employee_name = user.get('name')

    # Get user's TODOs
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(todos_url)
    todos = response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Print the output
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
        get_employee_todo_progress(emp_id)
    except ValueError:
        print("Please enter a valid integer for employee ID.")
        sys.exit(1)
