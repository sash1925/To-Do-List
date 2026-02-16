class ToDoList:

    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        task_dict = {
            "task": task,
            "done": False
        }
        self.tasks.append(task_dict)


    def view_task(self):
        for index, task in enumerate(self.tasks):
            print(index + 1, ".", task["task"], "-", task["done"])


    def update_task(self, user_id, new_title, new_status):
        index = user_id - 1

        if index >= 0 and index < len(self.tasks):
            self.tasks[index]["task"] = new_title
            self.tasks[index]["done"] = new_status
        else:
            print("Invalid ID")


    def delete_task(self, user_id):
        index = user_id - 1

        if index >= 0 and index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid ID")


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
        user_id = int(input("Enter task number: "))
        new_title = input("Enter new title: ")
        status_input = input("Is task done? (yes/no): ")

        if status_input.lower() == "yes":
            new_status = True
        else:
            new_status = False

        todo.update_task(user_id, new_title, new_status)

    elif choice == "3":
        user_id = int(input("Enter task number: "))
        todo.delete_task(user_id)

    elif choice == "4":
        todo.view_task()

    elif choice == "5":
        break

    else:
        print("Invalid choice")
