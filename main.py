task = []
tasks =[]
def addTask():
    task = input("Please enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f'Task #{index+1} {task}')

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
        else:
            print(f'Task #{taskToDelete} was not found.')
    except:
        print("Invalid input.")

if __name__ == '__main__':
    # Create a loop to run the loop
    print('Welcome to the to do list app')
    while True:
        print("\n")
        print("Please select one of the following options")
        print("-------------------------------------------")
        print("1. Add a new task to the list")
        print("2. Delete the task from the list")
        print("3. List of tasks")
        print("4. Quit")

        choice = input("Enter a choice:")
        if choice =="1":
            addTask()
        elif choice =="2":
            deleteTask()
        elif choice =="3":
            listTasks()
        elif choice =="4":
            break
        else:
            print("Invalid choice")

        print("Goodbye !!!") 
