def task_manager():
    task = []  # Empty List
    print("------Welcome To Task Management App------")
    total_tasks = int(input("Enter The Number of Tasks You Want To Add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter Task {i}: ")
        task.append(task_name)
    
    print(f"Today's Tasks Are:\n{task}")

    while True:
        operation = int(input("\nEnter:\n 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Exit\nChoice: "))
        if operation == 1:
            add = input("Enter The Task That You Want To Add: ")
            task.append(add)
            print(f"Task '{add}' has been Successfully added...")
        elif operation == 2:
            updated_val = input("Enter the task that you want to update: ")
            if updated_val in task:
                up = input("Enter new task: ")
                ind = task.index(updated_val)
                task[ind] = up
                print(f"Updated task to '{up}'")
            else:
                print("Task not found.")
        elif operation == 3:
            del_val = input("Enter which task you want to delete: ")
            if del_val in task:
                ind = task.index(del_val)
                del task[ind]
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found.")
        elif operation == 4:
            print(f"Total Tasks: {task}")
        elif operation == 5:
            print("Closing the program.....")
            break
        else:
            print("Invalid Input!")

# Run the function
task_manager()
