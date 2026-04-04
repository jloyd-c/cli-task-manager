# empty list for tasks
task = []

# function to display options
def option():
    print("======== MENU ========")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Exit")

# function to add task
def add_task(user):
    task.append(user)
    print("Task added successfully!")

# function to view task
def list_task():
    for index, list_tasks in enumerate(task, start=1):
        print(f"{index}. {list_tasks}")

# main system
while True:
    option()
    try:
        user = int(input("Choose an option: "))
    except ValueError:
        print("Invalid Input, Please Enter a number!")
        continue

    if user == 1:
        user_task = input("Enter a new task: ").strip()
        if len(user_task) == 0:
            print("Empty Task is not allowed!")
            continue
        add_task(user_task)

    elif user == 2:
        if len(task) == 0:
            print("Empty list")
        else:
            list_task()

# Stop the system
    elif user == 4:
        break