import click # to create a cli
import json # to read and write to the json file
import os # to check if the file exists

# to create a todo list

TODO_FILE = "todo.json" # to store the todo list

# do function banege ek file ko save krne k liye
# or ek function banege jo file ko load karega

# ek function banega phr is m if statement laga ke check karega ki file exist karta hy ya nahi
# agar nahi hai toh ek message dikhayega ki file nahi hai
# agar hai toh ek message dikhayega ki file hai
# or ek function banega jo file ko load karega

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return [] # if the file does not exist, return an empty list
    with open(TODO_FILE, "r") as file: # if the file exists, open it and load the todos
        return json.load(file) # return the todos

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file: # "w" means write mode file write karega as  file ye ek varailbe hai jiska naam file hai
        json.dump(tasks, file, indent=4) # json.dump ek function hai jo tasks ko json format m convert karega and file m save karega indent=4 means 4 spaces se save karega

# decorator function banega jo check karega ki file exist karta hy ya nahi
@click.group()

def cli():
    """Simple CLI for managing your todo list"""
    pass # pass ka kam hai ki function ko run karega

@click.command()
@click.argument("task")
def add(task):
    """Add a new todo"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}") #echo ek function hai jo task ko print karega

@click.command()
def list():
    """List all todos"""
    tasks = load_tasks()
    if not tasks: #not ka kam hai ki agar tasks empty hai toh No todos found dikhayega
        click.echo("No todos found")
        return
    for index, task in enumerate(tasks, 1): #enumerate ek function hai jo task ko index se print karega
        status = "✓" if task["done"] else "X"
        click.echo(f"{index}. {task['task']} [{status}]") #f string ka kam hai ki task ko print karega

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a todo as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Delete a todo"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo(f"Invalid task number: {task_number}")

cli.add_command(add) # add_command ek function hai jo add ko ye click arha hy
cli.add_command(list) # add_command ek function hai jo list ko ye click arha hy
cli.add_command(complete) # add_command ek function hai jo complete ko ye click arha hy
cli.add_command(remove) # add_command ek function hai jo remove ko ye click arha hy
if __name__ == "__main__":
    cli() # cli ek function hai jo click arha hy


# all commands
# uv run python todo.py add "Buy grocery for sehri and iftari"
# uv run python todo.py list
# uv run python todo.py complete 1
# uv run python todo.py remove 1
































# import click  # Import the `click` library to create a CLI
# import json  # Import `json` to save and load tasks from a file
# import os  # Import `os` to check if the file exists

# TODO_FILE = "todo.json"  # Define the filename where tasks are stored


# # Function to load tasks from the JSON file
# def load_tasks():
#     if not os.path.exists(TODO_FILE):  # Check if file exists
#         return []  # If not, return an empty list
#     with open(TODO_FILE, "r") as file:  # Open the file in read mode
#         return json.load(file)  # Load and return the JSON data as a Python list


# # Function to save tasks to the JSON file
# def save_tasks(tasks):
#     with open(TODO_FILE, "w") as file:  # Open the file in write mode
#         json.dump(tasks, file, indent=4)  # Save tasks as formatted JSON


# @click.group()  # Define a Click command group (main CLI)
# def cli():
#     """Simple To-Do List Manager"""  # Docstring for the CLI
#     pass  # No action, acts as a container for commands


# @click.command()  # Define a command called 'add'
# @click.argument("task")  # Accepts a required argument (task name)
# def add(task):
#     """Add a new task to the list"""
#     tasks = load_tasks()  # Load existing tasks
#     tasks.append({"task": task, "done": False})  # Append a new task (default: not done)
#     save_tasks(tasks)  # Save the updated tasks
#     click.echo(f"Task added: {task}")  # Print a success message


# @click.command()  # Define a command called 'list'
# def list():
#     """List all tasks"""
#     tasks = load_tasks()  # Load existing tasks
#     if not tasks:  # If there are no tasks
#         click.echo("No tasks found!")  # Print message
#         return  # Stop execution
#     for index, task in enumerate(tasks, 1):  # Loop through tasks with numbering
#         status = "✓" if task["done"] else "✗"  # Show '✓' for completed, '✗' for not
#         click.echo(f"{index}. {task['task']} [{status}]")  # Print task with status


# @click.command()  # Define a command called 'complete'
# @click.argument("task_number", type=int)  # Accepts a task number as an integer
# def complete(task_number):
#     """Mark a task as completed"""
#     tasks = load_tasks()  # Load existing tasks
#     if 0 < task_number <= len(tasks):  # Ensure task number is valid
#         tasks[task_number - 1]["done"] = True  # Mark as done
#         save_tasks(tasks)  # Save updated tasks
#         click.echo(f"Task {task_number} marked as completed!")  # Print success message
#     else:
#         click.echo("Invalid task number.")  # Handle invalid numbers


# @click.command()  # Define a command called 'remove'
# @click.argument("task_number", type=int)  # Accepts a task number as an integer
# def remove(task_number):
#     """Remove a task from the list"""
#     tasks = load_tasks()  # Load existing tasks
#     if 0 < task_number <= len(tasks):  # Ensure task number is valid
#         removed_task = tasks.pop(task_number - 1)  # Remove the task
#         save_tasks(tasks)  # Save updated tasks
#         click.echo(f"Removed task: {removed_task['task']}")  # Print removed task
#     else:
#         click.echo("Invalid task number.")  # Handle invalid numbers


# # Add commands to the main CLI group
# cli.add_command(add)
# cli.add_command(list)
# cli.add_command(complete)
# cli.add_command(remove)

# # If the script is run directly, start the CLI
# if __name__ == "__main__":
#     cli()