#!/usr/bin/python3
"""Using REST API, for a given employee ID,
returns information about his/her TODO list progress.

Script to export data in the JSON format.
"""

import json
import requests
import sys


def get_employee_info(user_id):
    """Function to export data in the JSON format."""
    """URL of the API endpoint"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f'{url}/users/{user_id}'
    todo_url = f'{url}/todos?userId={user_id}'

    try:
        user_res = requests.get(user_url)
        todo_res = requests.get(todo_url)
        user_res_data = requests.get(user_url).json()
        todo_res_data = requests.get(todo_url).json()

        if user_res.status_code == 200 and todo_res.status_code == 200:
            employee_name = user_res_data.get('name')

            json_filename = f'{user_id}.json'
            tasks = [{"task": task['title'],
                      "completed": task['completed'],
                      "username": employee_name}
                     for task in todo_res_data]

            with open(json_filename, mode='w', encoding='utf-8') as json_file:
                json.dump({str(user_id): tasks}, json_file, indent=2)

            print(f"Data exported to {json_filename}")
            print(f"Number of tasks found: {len(tasks)}")
        else:
            print(f"Failed to fetch data for employee {user_id}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """Check if an employee ID is provided as a command-line argument"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    get_employee_info(user_id)
