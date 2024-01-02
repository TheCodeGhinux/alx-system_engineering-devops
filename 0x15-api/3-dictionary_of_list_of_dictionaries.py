#!/usr/bin/python3
"""Using REST API, for a given employee ID,
returns information about his/her TODO list progress.

Script to export data in the JSON format.
To get all Employees
"""

import csv, sys, requests
import json

def get_all_employee(user_id):
    """Function to export all employee data in the JSON format."""
    """URL of the API endpoint"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f'{url}/users'
    json_data = {}

    try:
        users_response = requests.get(user_url)
        users_response_data = requests.get(user_url).json()

        if users_response.status_code == 200:
            for user in users_response_data:
                user_id = str(user['id'])
                username = user['name']

                """Fetch TODO list for each user"""
                response_todos = requests.get(f'{user_url}/{user_id}/todos')
                todos = response_todos.json()

                if response_todos.status_code == 200:
                    json_data[user_id] = [{"username": username, "task": task['title'], "completed": task['completed']} for task in todos]
                else:
                    print(f"Failed to fetch TODO list for user {user_id}")

            """Create the JSON file"""
            json_filename = 'todo_all_employees.json'
            with open(json_filename, mode='w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=2)

            print(f"Data exported to {json_filename}")

        else:
            print("Failed to fetch user data")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_all_employee()
