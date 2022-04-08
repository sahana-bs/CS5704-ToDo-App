from django.shortcuts import render, redirect
from .models import TaskList, regular_users, TaskLists, admin_user, completed_tasks, \
    pending_task


# Create your views here.

# function to render to Add an item page.
def task_item(request):
    if 'username' in request.session:
        if request.session['role'] == "admin":
            return render(request,
                          "library/library_store/addItem.html")
        else:
            return render(request,
                          "library/library_store/home.html",
                          {"completedtasks": completed_tasks, "pendingtasks": pending_task})
    else:
        return render(request,
                      "library/library_store/home.html",
                      {"completedtasks": completed_tasks, "pendingtasks": pending_task})


# function to create an entry in the lists page.
def createTaskItem(request):
    id = 1
    title = request.POST.get("Title")
    description = request.POST.get("description")
    assigned_by = request.POST.get("author")
    assigned_to = request.POST.get("assigned")
    category = request.POST.get("category")
    priority = request.POST.get("priority")
    img = request.POST.get("upload-image")
    if img:
        img = "img/" + img
    id += len(TaskList)
    ratings = 0
    bookItem = TaskLists(id, img, title, assigned_by, assigned_to, category, priority, description)
    TaskList.append(bookItem)
    return task_item_list(request)



