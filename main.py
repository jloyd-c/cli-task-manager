# empty list for tasks
task = []

# function to display options
def option():
    print("======== MENU ========")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Edit Task")
    print("6. Exit")

# function to add task
def add_task(user):
    task.append(user)
    print("Task added successfully!")

# function to view task
def list_task():
    for index, list_tasks in enumerate(task, start=1):
        if list_tasks['mark'] == True:
            check_mark = "[✔]"
        else:
            check_mark = "[ ]"
        print(f"{check_mark} {index}. {list_tasks['task']}")

# function to mark task done
def mark_task(user_input):
    for index, list_tasks in enumerate(task, start=1):
        if index == user_input:
            list_tasks['mark'] = True

        if list_tasks['mark'] == True:
            check_mark = "[✔]"
        else:
            check_mark = "[ ]"

        print(f"{check_mark} {index}. {list_tasks['task']}")

        

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
        new_task = {
            "task" : user_task,
            "mark" : False
            }
        add_task(new_task)

    elif user == 2:
        if len(task) == 0:
            print("Empty list")
        else:
            list_task()

    elif user == 3:
        list_task()
        try:
            user_mark_task = int(input("Choose task to mark done: "))
        except ValueError:
            print("Invalid Input, Please Enter a number!")
            continue

        mark_task(user_mark_task)

    elif user == 4:
        list_task()
        try:
            user_delete_task = int(input("Choose task to delete: "))
        except ValueError:
            print("Invalid Input, Please Enter a number!")
            continue

        if len(task) >= user_delete_task and  user_delete_task > 0:
            task.pop(user_delete_task - 1)
            print("Task Deleted!")
        else:
            print("Invalid input!")

    elif user == 5:
        list_task()
        try:
            user_edit_task = int(input("Choose task to edit: "))
        except ValueError:
            print("Invalid Input, Please Enter a number!")
            continue

        if len(task) >= user_edit_task and  user_edit_task > 0:
            edit_task = input("Enter new task: ")
            
            task[user_edit_task - 1]["task"] = edit_task
        
        
# Stop the system
    elif user == 6:
        break