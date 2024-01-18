class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

def add_task(tasks, description):
    new_task = Task(description)
    tasks.append(new_task)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print(f"{'Index':<5}{'Description':<25}{'Status':<15}")
        print("------------------------------------------")
        for i, task in enumerate(tasks):
            status = "Completed" if task.completed else "Pending"
            print(f"{i:<5}{task.description:<25}{status:<15}")

def mark_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        print("Task marked as completed.")
    else:
        print("Invalid index.")

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task removed successfully.")
    else:
        print("Invalid index.")

def main():
    tasks = []

    print("Simple To-Do List Manager\n")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter the task description: ")
            add_task(tasks, description)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(tasks, index)
        elif choice == "4":
            index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
Simple To-Do List Manager


Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Quit
Task added successfully.

Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Quit
Task added successfully.

Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Quit
IndexDescription              Status         
------------------------------------------
0    i will sleep             Pending        
1    i will eat               Pending        

Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Quit
Task marked as completed.

Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Quit
IndexDescription              Status         
------------------------------------------
0    i will sleep             Completed      
1    i will eat               Pending        

Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Quit
Task removed successfully.

Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Quit
IndexDescription              Status         
------------------------------------------
0    i will eat               Pending        

Options:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Quit