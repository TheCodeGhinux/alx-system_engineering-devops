#!/usr/bin/python3
"""Using REST API, for a given employee ID,
returns information about his/her TODO list progress.

Script to export data in the JSON format.
To get all Employees
"""

import requests
import sys


def get_employee_info(employee_id):
    """Function to get all employee data in the JSON format."""
    """URL of the API endpoint"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f'{url}/users/{employee_id}'
    response = requests.get(user_url)

    if response.status_code == 200:
        employee_name = response.json().get('name')

        todo_url = f'{url}/todos?userId={employee_id}'
        todo_response = requests.get(todo_url)

        if todo_response.status_code == 200:
            todo_data = todo_response.json()

            completed_tasks = [task for task in todo_data if task['completed']]
            num_completed_tasks = len(completed_tasks)
            total_tasks = len(todo_data)

            print(f"Employee {employee_name} is done with task
                  ({num_completed_tasks}/{total_tasks}): ")
            for task in completed_tasks:
                print(f"    {task['title']}")

        else:
            print(f"Failed to fetch TODO list for employee {employee_id}")
    else:
        print(f"Failed to fetch employee information for ID {employee_id}")


if __name__ == "__main__":
    """Check if an employee ID is provided as a command-line argument"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
