# Task Manager CLI (Command Line Interface)


tasks =[]
def show_menu():
    print("\n============= TASK MANAGER ================")
    print("1. Add Task")
    print("2. View All Task")
    print("3. Mark Task As Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    if not tasks:
        print("Task list is empty . Adding your first task. ")
    task = input("\nEnter a new task : ")
    tasks.append(task)
    print("\nTask added successfully!")
    show_menu()
    choose_option()

def view_all_task():
    print("=============LIST OF TASKS=============")
    for idx , task in enumerate(tasks , start =1):
        print(f"{idx}. {task}")
    show_menu()
    choose_option()

def mark_done():
    print(3)
def delete_task():
    print(4)
def exit_menu():
    print(5)


def choose_option():
    option = int(input("\nChoose an option (1-5) : "))
    if option == 1:
        add_task()
    elif option == 2:
        view_all_task()
#   elif option == 3:
#       mark_done()
#   elif option == 4:
#       delete_task()
#   elif option == 5:
#       exit_menu()
    else:
        print("Choice is not valid . \n TRY AGAIN!!")

show_menu()
choose_option()


