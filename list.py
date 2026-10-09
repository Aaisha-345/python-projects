import os

def load_tasks():
    """Challenge Feature: Loads tasks from a text file if it exists."""
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        tasks.append({
                            "name": parts[0],
                            "done": parts[1] == "True",
                            "priority": parts[2]
                        })
    return tasks

def save_tasks(tasks):
    """Challenge Feature: Saves tasks to a text file."""
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task['name']}|{task['done']}|{task['priority']}\n")

def show_tasks(tasks):
    """MVP Feature: Displays all current tasks with their status and IDs."""
    if not tasks:
        print("\n Your to-do list is empty! (Edge case verified)")
        return
    
    print("\n--- Current To-Do List ---")
    for index, task in enumerate(tasks, start=1):
        status = "[✓] Done   " if task["done"] else "[ ] Pending"
        priority = task["priority"].upper()
        print(f"{index}. {status} | Priority: {priority} | {task['name']}")
    print("-" * 35)

def add_task(tasks):
    """MVP Feature: Appends a new task with a specified priority level."""
    name = input("\nEnter the task description: ").strip()
    if not name:
        print("Task cannot be empty!")
        return
    
    priority = input("Enter priority (High/Medium/Low) [Default: Medium]: ").strip().lower()
    if priority not in ["high", "medium", "low"]:
        priority = "medium"
        
    tasks.append({"name": name, "done": False, "priority": priority})
    print(f" Task '{name}' added successfully!")

def mark_task_done(tasks):
    """Improvement Feature: Marks a specific task as completed using its ID."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter the number of the task to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print(f" Task {choice} marked as done!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a numerical ID.")

def delete_task(tasks):
    """Improvement Feature: Removes a task from the list using its ID."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f" Deleted task: '{removed['name']}'")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a numerical ID.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("\nProgress saved. Goodbye!")
            break
        else:
            print(" Invalid choice. Please pick between 1 and 5.")

if __name__ == "_main_":
    main()