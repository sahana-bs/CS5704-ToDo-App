from django.db import models


# Create your models here.
class TaskLists:
    def __init__(self, id, img, title, assigned_by, assigned_to, category, priority, description):
        self.id = id
        self.img = img
        self.title = title
        self.assigned_by = assigned_by
        self.assigned_to = assigned_to
        self.category = category
        self.priority = priority
        self.description = description


taskItem1 = TaskLists(
    1,
    "img/event1.jpg",
    "Design Document",
    "Chris Brown",
    "Disha Bhan",
    "SE Project",
    "High",
    "To add the constraints of the design arch in the design doc."
)

taskItem2 = TaskLists(
    2,
    "img/event2.jpg",
    "Design Document",
    "Chris Brown",
    "Disha Bhan",
    "SE Project",
    "High",
    "To add the constraints of the design arch in the design doc."
)

taskItem3 = TaskLists(
    3,
    "img/event3.jpg",
    "Design Document",
    "Chris Brown",
    "Disha Bhan",
    "SE Project",
    "High",
    "To add the constraints of the design arch in the design doc."
)

taskItem4 = TaskLists(
    4,
    "img/event4.jpg",
    "Design Document",
    "Chris Brown",
    "Disha Bhan",
    "SE Project",
    "High",
    "To add the constraints of the design arch in the design doc."
)

taskItem5 = TaskLists(
    5,
    "img/event5.jpg",
    "Design Document",
    "Chris Brown",
    "Disha Bhan",
    "SE Project",
    "High",
    "To add the constraints of the design arch in the design doc."
)
taskItem6 = TaskLists(
    6,
    "img/event6.jpg",
    "Design Document",
    "Chris Brown",
    "Disha Bhan",
    "SE Project",
    "High",
    "To add the constraints of the design arch in the design doc."
)

TaskList = []
TaskList.append(taskItem1)
TaskList.append(taskItem2)
TaskList.append(taskItem3)
TaskList.append(taskItem4)
TaskList.append(taskItem5)
TaskList.append(taskItem6)

completed_tasks = []
completed_tasks.append(taskItem1)
completed_tasks.append(taskItem2)
completed_tasks.append(taskItem3)
completed_tasks.append(taskItem4)

pending_task = []
pending_task.append(taskItem5)
pending_task.append(taskItem6)

regular_users = {"username": "chris", "password": "regular"}
admin_user = {"username": "admin", "password": "admin"}


