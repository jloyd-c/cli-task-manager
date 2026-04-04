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

# Stop the system
    if user == 4:
        break