class Task: #class Task
    def __init__(self, title, description="", status="incomplete"): #constructor
        #initialization
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self): #fucntion to mark task as complete
        self.status = "complete"

    def to_s(self): #function to return printable format of the task
        return f"Task: {self.title} - Status: {self.status}"
    

class PriorityTask(Task): # priorityTask inherits from Task
    def __init__(self, title, description="", status="incomplete", priority="low"): # priority tasks have an additional priority attribute (e.g., low, medium, high).
        super().__init__(title, description, status) #method overriding of the common part of the task from parent class.
        self.priority = priority #setting the priority of task

    def mark_complete(self):
        super().mark_complete() # method overriding to mark priority task as complete.

    def to_s(self):
        return f"{super().to_s()} - Priority: {self.priority}" # method overriding to fetch the common output from super class Task.

class TaskList: # TaskList class for implementing listing of tasks 
    def __init__(self): # constructor to initialize a TaskList with an empty list of normal tasks and priority task.
        self.tasks = []
        self.priority_tasks = []

    def add_task(self, title, description=None, status="incomplete"): # method to ddd a tasks using the concept of method overloading
        if description is not None:
            new_task = Task(title, description, status) # creating task with description
        else:
            new_task = Task(title, status=status) # creating task without description
        self.tasks.append(new_task) # adding task to the list of tasks

    def remove_task(self, title): #function to remove a task
        for task in self.tasks:
            if task.title == title: # idetifying task with title
                self.tasks.remove(task) # removing task from the list of tasks

    def list_tasks(self): #function to list the task
        for task in self.tasks:
            print(task.to_s())

    def list_priority_tasks(self): #function to list the priority task
        for ptask in self.priority_tasks:
            print(ptask.to_s())

    def add_priority_task(self, title, description="", priority="low"): # method to ddd a tasks using the concept of method overloading
        if description is not None:
            new_priority_task = PriorityTask(title, description, "incomplete", priority) # creating priority task with description
        else:
            new_priority_task = PriorityTask(title, "incomplete", priority) # creating priority task without description
        self.priority_tasks.append(new_priority_task) #addind priority to the list of priority task

    def find_task(self, title): #function to find a task using title
        for task in self.tasks: 
            if task.title == title:
                return task #returning the task in object form
    
    def find_priority_task(self, title): #function to find a priority task using title
        for ptask in self.priority_tasks: 
            if ptask.title == title:
                return ptask #returning the priority task in object form

task_list = TaskList()
task_list.add_task("Do homework")
task_list.add_task("Go to the gym", "Cardio workout")
task_list.find_task("Go to the gym").mark_complete()
task_list.list_tasks()
task_list.add_priority_task("Buy groceries", "Milk and eggs", "high")
print(task_list.find_task("Do homework").to_s())
print(task_list.find_priority_task("Buy groceries").to_s())
# Output:
# Task: Do homework - Status: incomplete
# Task: Go to the gym - Status: incomplete
# Task: Do homework - Status: incomplete
# Task: Buy groceries - Status: incomplete - Priority: high