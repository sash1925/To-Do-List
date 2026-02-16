class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        new_task = {
            "task" : task,
            "status" : False
        }

        self.tasks.append(new_task)

    def view_task(self):
        if len(self.tasks) == 0:
            print("No tasks found")
        else:
            count = 1
            for t in self.tasks:
                print(count, ".", t["task"], "-", t["status"])
                count = count + 1

    def update_task(self, task_number, new_title, new_status):
        index = task_number - 1

        if index >= 0 and index < len(self.tasks):
            self.tasks[index]["task"] = new_title
            self.tasks[index]["status"] = new_status
            print("Task updated")
        else:
            print("Invalid number")

    def delete_task(self, task_number):
        index = task_number - 1
        if index >= 0 and index < len(self.tasks):
            self.tasks.pop(index)
            print("Task deleted")
        else:
            print("Invalid number")


todo = ToDoList()

while True:
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. View Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        todo.add_task(title)

    elif choice == "2":
        task_number = int(input("Enter task number: "))
        new_title = input("Enter new title: ")
        new_status = input("Is task done? (yes/no): ")

        if new_status.lower() == "yes":
            new_status = True
        else:
            new_status = False

        todo.update_task(task_number, new_title, new_status)

    elif choice == "3":
        user_id = int(input("Enter task number: "))
        todo.delete_task(user_id)

    elif choice == "4":
        todo.view_task()

    elif choice == "5":
        break

    else:
        print("Invalid choice")



