# Function to display all tasks
def show_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nYour to-do list is empty.")
    print("\n")

# Function to add a new task
def add_task(tasks):
    task = input("What is the new task? ")
    tasks.append(task)
    print(f"'{task}' has been added to your list.\n")

# Function to remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task you want to remove: "))
        if 0 < task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            print(f"'{task}' has been removed.\n")
        else:
            print("That task number doesn't exist.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to save tasks to a file
def save_tasks(tasks):
    with open("todo_list.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Your tasks have been saved.\n")

# Function to load saved tasks
def load_tasks():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = [task.strip() for task in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

# Main function to run the to-do list app
def main():
    tasks = load_tasks()  # Load saved tasks from file
    while True:
        print("Welcome to your To-Do List!")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Save and Exit")
        
        choice = input("What would you like to do? (1/2/3/4): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please choose between 1, 2, 3, or 4.\n")

# Start the program
if __name__ == "__main__":
    main()

