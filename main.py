import json


# ---------- FILE HANDLING ----------

def save_tasks(tasks):

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():

    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# ---------- TASK FUNCTIONS ----------

def add_task(tasks):

    task_name = input("\nEnter task name: ")

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):

    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    print("\n===== Your Tasks =====")

    for index, task in enumerate(tasks, start=1):

        status = "Completed" if task["completed"] else "Pending"

        print(f"{index}. {task['name']} - {status}")


def complete_task(tasks):

    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        complete_index = int(
            input("\nEnter task number to complete: ")
        ) - 1

        if 0 <= complete_index < len(tasks):

            tasks[complete_index]["completed"] = True

            save_tasks(tasks)

            print("Task marked as completed!")

        else:
            print("Invalid task number")

    except ValueError:
        print("Please enter a valid number")


def delete_task(tasks):

    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        delete_index = int(
            input("\nEnter task number to delete: ")
        ) - 1

        if 0 <= delete_index < len(tasks):

            removed_task = tasks.pop(delete_index)

            save_tasks(tasks)

            print(f"{removed_task['name']} deleted successfully!")

        else:
            print("Invalid task number")

    except ValueError:
        print("Please enter a valid number")


# ---------- MAIN PROGRAM ----------

def main():

    tasks = load_tasks()

    while True:

        print("\n===== Student Task Manager =====")

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":

            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ---------- START PROGRAM ----------

main()