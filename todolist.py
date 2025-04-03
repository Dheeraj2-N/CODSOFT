import json
import os
from datetime import datetime

class ToDoList:
    def __init__(self, filename="todo.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        
        print("\nTo-Do List:")
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            print(f"{task['id']}. [{status}] {task['description']} (Created: {task['created']})")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                # Reassign IDs to maintain order
                for j, t in enumerate(self.tasks[i:], start=i):
                    t["id"] = j + 1
                self.save_tasks()
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")

    def clear_completed(self):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task["completed"]]
        # Reassign IDs
        for i, task in enumerate(self.tasks):
            task["id"] = i + 1
        removed_count = initial_count - len(self.tasks)
        self.save_tasks()
        print(f"Removed {removed_count} completed tasks.")

def main():
    todo = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Clear Completed Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            description = input("Enter task description: ")
            todo.add_task(description)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            todo.clear_completed()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()