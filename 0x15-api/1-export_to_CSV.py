#!/usr/bin/python3
"""Using REST API, for a given employee ID,
returns information about his/her TODO list progress.

Script to export data in the CSV format.
"""

import csv, sys, requests

def get_employee_info(employee_id):
    """Function to export data in the CSV format."""
    """URL of the API endpoint"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f'{url}/users/{employee_id}'
    todo_url = f'{url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_response_data = requests.get(user_url).json()
        todo_response_data = requests.get(todo_url).json()


        if user_response.status_code == 200 and todo_response.status_code == 200:
            employee_name = user_response_data.get('name')

            """Create the CSV file"""
            csv_filename = f'{employee_id}.csv'
            with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                for task in todo_response_data:
                    task_completed_status = str(task['completed'])
                    task_title = task['title']
                    csv_writer.writerow([employee_id, employee_name, task_completed_status, task_title])

            print(f"Data exported to {csv_filename}")
        else:
            print(f"Failed to fetch data for employee {employee_id}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    """Check if an employee ID is provided as a command-line argument"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
