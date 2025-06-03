# Task Manager CLI (Command Line Interface)


tasks =[]
def show_menu():
    print("\n============= TASK MANAGER ================")
    print("1. View All Task")
    print("2. Add Task")
    print("3. Mark Task As Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    if not tasks:
        print("Task list is empty . Adding your first task. ")
    title = input("\nEnter a new task : ")
    tasks.append({"title" : title ,"done" : False})
    print("\nTask added successfully!")

def view_all_task():
    print("\n============= LIST OF TASKS ================\n")
    if not tasks:
        print("LIST IS EMPTY NOW")
    for idx , task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{idx+1}. {task['title']} [{status}] ")

def mark_done():
    view_all_task()
    index = int(input("\nEnter The Task Number To Mark As Done : "))
    tasks[index-1]["done"] = True
    print(f"\nMarked '{tasks[index-1]["title"]}' As Done !!")


def delete_task():
    view_all_task()
    delete = int(input("\nEnter the Task Number To Remove : "))
    if 1 <= delete <= len(tasks):
        removed_task =tasks.pop(delete-1)
        print(f"\nTask '{removed_task["title"]}' Removed Successfully !")
    else:
        print("\nInvalid Taks Number ")


while True:
    show_menu()
    option = int(input("\nChoose an option (1-5) : "))
    if option == 1:
        view_all_task()
    elif option == 2:
        add_task()  
    elif option == 3:
        mark_done()
    elif option == 4:
        delete_task()
    elif option == 5:
        print("\n THANKS TO VISIT !")
        break
    else:
        print("\nChoice is not valid .TRY AGAIN!!")




