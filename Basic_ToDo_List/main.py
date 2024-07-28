tasks = []

def addTask():
  task = input("Enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added successfully!")


def list_task():
  if not tasks:
    print("There are no tasks")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task #{index}. {tasks}")


def deleteTask():
  list_task()
  try:
    task_to_delete = int(input("Enter # of tasks to delete: "))
    if task_to_delete >=0 and task_to_delete < len(tasks):
      tasks.pop(task_to_delete)
      print(f"Task {task_to_delete} has been deleted")
    else:
      print(f"Task #{task_to_delete} does not exist.")
  except:
    print("Invalid input")


if __name__ == "__main__":
  ##create a loop to run app 
  print("Welcome to the To-Do List App")
  while True:
    print("Please select an option")
    print("-----------------------")
    print("1. Add a new task")
    print("2. delete a task")
    print("3. list tasks")
    print("4. quit")

    choice = input("Enter your choice (1-4): ")
    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      list_task()
    elif (choice == "4"):
      break
    else:
      print("Invalid choice. Please try again.")
      
  print("Thank you for using the To-Do List App")
