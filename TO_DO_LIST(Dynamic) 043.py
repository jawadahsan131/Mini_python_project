import json

class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append({"task": task, "completed":False})
        print(f"Task -> {task} <- added to the list.")
    def remove_task(self,task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Task {removed_task['task']} removed from the list.")
        else:
            print("Invalid task number.")
    def mark_completed(self,task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f"Task {self.tasks[task_number]["task"]} marked as completed.")
        else:
            print("Invalid task number.")
    def view_task(self):
        if not self.tasks:
            print("No tasks in the to do list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "incomplete"
                print(f"{i + 1}. {task["task"]} - {status}")
    def save_tasks(self,filename = "todo_list.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file, indent=4)
        print(f"Tasks saved to {filename}")
    def load_tasks(self,filename = "todo_list.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
            print(f"TAsks loaded from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found. starting with an empty list.")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()
    Flag = True
    while Flag:
        print("\n--- Main Menu ---")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Remove Tasks")
        print("4. Mark task as completed")
        print("5. Save taks")
        print("6. Exit")
        choice = input("Choose an option (1 - 6):")
        if choice == "1":
            todo_list.view_task()
        elif choice == "2":
            task = input("enter the task:")
            todo_list.add_task(task)
        elif choice == "3":
            todo_list.view_task()
            task_number = int(input("Enter the taask number to remove:"))
            todo_list.remove_task(task_number)
        elif choice == "4":
            todo_list.view_task()
            task_number = int(input("Enter the task number to mark as complete:")) - 1
            todo_list.mark_completed(task_number)
        elif choice == "5":
            todo_list.save_tasks()
        elif choice == "6":
            print("Exiting and saving tasks...")
            break
        else:
            print("Invalid option. Please choose a number 1 and 6.")


if __name__ == "__main__":
    main()