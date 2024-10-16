class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.id}. {self.title} - {status}"
tasks = []

def add_task(title):
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task)

def view_tasks():
    for task in tasks:
        print(task)

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]

def mark_task_complete(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
import json

def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as file:
            tasks_data = json.load(file)
            tasks = [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        tasks = []
def main():
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to complete: "))
            mark_task_complete(task_id)
        elif choice == "5":
            save_tasks()
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
