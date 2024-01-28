class Task:
    def __init__(self, title, description="", status="incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self):
        self.status = "complete"

    def to_s(self):
        return f"Task: {self.title} - Status: {self.status}"
    

class PriorityTask(Task): # priorityTask inherits from Task
    def __init__(self, title, description="", status="incomplete", priority="low"): # priority tasks have an additional priority attribute (e.g., low, medium, high).
        super().__init__(title, description, status)
        self.priority = priority

    def mark_complete(self):
        super().mark_complete() # method overriding to mark priority task as complete.

    def to_s(self):
        return f"{super().to_s()} - Priority: {self.priority}" # method overriding to fetch the common output from super class Task.

class TaskList: # TaskList class for implementing listing of tasks 
    def __init__(self): # constructor to initialize a TaskList with an empty list of tasks.
        self.tasks = []
        self.priority_tasks = []

    def add_task(self, title, description=None, status="incomplete"): # method to ddd a task
        if description is not None:
            new_task = Task(title, description, status)
        else:
            new_task = Task(title, status=status)
        self.tasks.append(new_task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task.to_s())

    def list_priority_tasks(self):
        for ptask in self.priority_tasks:
            print(ptask.to_s())

    def add_priority_task(self, title, description="", priority="low"):
        new_priority_task = PriorityTask(title, description, "incomplete", priority)
        self.priority_tasks.append(new_priority_task)

    def find_task(self, title):
        for task in self.tasks: 
            if task.title == title:
                return task
    
    def find_priority_task(self, title):
        for ptask in self.priority_tasks: 
            if ptask.title == title:
                return ptask

task_list = TaskList()
task_list.add_task("Do homework")
task_list.add_task("Go to the gym", "Cardio workout")
task_list.list_tasks()
task_list.add_priority_task("Buy groceries", "Milk and eggs", "high")
task_list.find_task("Go to the gym").mark_complete()
print(task_list.find_task("Do homework").to_s())
print(task_list.find_priority_task("Buy groceries").to_s())
task_list.find_priority_task("Buy groceries").mark_complete()
print(task_list.find_priority_task("Buy groceries").to_s())
# Output:
# Tasks:
# Task: Do homework - Status: incomplete
# Task: Go to the gym - Status: complete
# Task: Do homework - Status: incomplete
# Priority Task: Buy groceries - Status: incomplete - Priority: high