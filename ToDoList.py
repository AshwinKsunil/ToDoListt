import os
TODO_FILE = "todo_list.txt"
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, 'r') as f:
            tasks = [line.strip() for line in f if line.strip()]
        return tasks
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []
def save_tasks(tasks):
    try:
        with open(TODO_FILE, 'w') as f:
            for task in tasks:
                f.write(task + '\n')
    except Exception as e:
        print(f"Error saving tasks: {e}")
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty. Time to relax!")
        return
    print("\n--- Current To-Do List ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("--------------------------")

def add_task(tasks):
    task_description = input("Enter the new task: ").strip()
    if task_description:
        new_task = f"[ ] {task_description}"
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added: '{task_description}'")
    else:
        print("Task cannot be empty.")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_index = int(input("Enter the number of the task to mark complete: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if 0 <= task_index < len(tasks):
        old_task = tasks[task_index]
        if old_task.startswith("[x]"):
            print("Task is already complete!")
            return
        new_task = old_task.replace("[ ]", "[x]", 1)
        tasks[task_index] = new_task
        save_tasks(tasks)
        print(f"Task marked complete: {tasks[task_index]}")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task deleted: {deleted_task}")
    else:
        print("Invalid task number.")
def main():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do Manager Menu ===")
        print("1. View To-Do List")
        print("2. Add New Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("\nSelect an option: ").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")
if __name__ == "__main__":
    main()
