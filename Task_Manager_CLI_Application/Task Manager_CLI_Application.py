'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

import json
import os

# Define a file for storing user data
USER_FILE = 'users.json'
TASKS_FILE = 'tasks.json'

# Load data from files if they exist, else initialize empty structures
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return {}

# Save data to a file
def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# Create a new account (POST)
def create_account():
    username = input("Enter your username: ")
    users = load_data(USER_FILE)

    if username in users:
        print("User already exists.")
    else:
        users[username] = []
        save_data(USER_FILE, users)
        print(f"Account created for {username}.")

# Create a new task (POST)
def create_task(username):
    tasks = load_data(TASKS_FILE)
    task_description = input("Enter the task description: ")
    task_status = input("Is the task completed? (yes/no): ").lower() == 'yes'

    if username not in tasks:
        tasks[username] = []

    task = {'description': task_description, 'completed': task_status}
    tasks[username].append(task)
    save_data(TASKS_FILE, tasks)
    print(f"Task added for {username}.")

# View all your tasks (GET)
def view_all_tasks(username):
    tasks = load_data(TASKS_FILE)

    if username in tasks:
        for idx, task in enumerate(tasks[username], start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{idx}. {task['description']} [{status}]")
    else:
        print("No tasks found.")

# View completed tasks (GET)
def view_completed_tasks(username):
    tasks = load_data(TASKS_FILE)

    if username in tasks:
        for idx, task in enumerate(tasks[username], start=1):
            if task['completed']:
                print(f"{idx}. {task['description']} [Completed]")
    else:
        print("No tasks found.")

# View incomplete tasks (GET)
def view_incomplete_tasks(username):
    tasks = load_data(TASKS_FILE)

    if username in tasks:
        for idx, task in enumerate(tasks[username], start=1):
            if not task['completed']:
                print(f"{idx}. {task['description']} [Incomplete]")
    else:
        print("No tasks found.")

# Update an existing task (PATCH/PUT)
def update_task(username):
    tasks = load_data(TASKS_FILE)

    if username in tasks and tasks[username]:
        view_all_tasks(username)
        task_num = int(input("Enter the task number to update: ")) - 1

        if 0 <= task_num < len(tasks[username]):
            new_description = input("Enter new task description (leave blank to keep the same): ")
            new_status = input("Is the task completed? (yes/no, leave blank to keep the same): ").lower()

            if new_description:
                tasks[username][task_num]['description'] = new_description
            if new_status in ['yes', 'no']:
                tasks[username][task_num]['completed'] = new_status == 'yes'

            save_data(TASKS_FILE, tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to update.")

# Delete a task (DELETE)
def delete_task(username):
    tasks = load_data(TASKS_FILE)

    if username in tasks and tasks[username]:
        view_all_tasks(username)
        task_num = int(input("Enter the task number to delete: ")) - 1

        if 0 <= task_num < len(tasks[username]):
            del tasks[username][task_num]
            save_data(TASKS_FILE, tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

# Menu for the application
def menu():
    username = input("Enter your username: ")

    while True:
        print("\nPlease select from the following options (enter the number):")
        print("1) Create a new account (POST)")
        print("2) View all your tasks (GET)")
        print("3) View your completed tasks (GET)")
        print("4) View only your incomplete tasks (GET)")
        print("5) Create a new task (POST)")
        print("6) Update an existing task (PATCH/PUT)")
        print("7) Delete a task (DELETE)")
        print("8) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            view_all_tasks(username)
        elif choice == '3':
            view_completed_tasks(username)
        elif choice == '4':
            view_incomplete_tasks(username)
        elif choice == '5':
            create_task(username)
        elif choice == '6':
            update_task(username)
        elif choice == '7':
            delete_task(username)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the application
if __name__ == "__main__":
    menu()
