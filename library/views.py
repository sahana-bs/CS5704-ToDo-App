from django.shortcuts import render, redirect
from .models import TaskList, regular_users, TaskLists, admin_user, completed_tasks, \
    pending_task, eventList


# Create your views here.
# function to render to the lists page.
def task_item_list(request):
    return render(request,
                  "library/library_store/list.html",
                  {"taskList": TaskList})


# function to render to the home page.
def todo_home(request):
    return render(request,
                  "library/library_store/home.html",
                  {"completedtasks": completed_tasks, "pendingtasks": pending_task})


# function to render to the login page.
def todo_login(request):
    return render(request,
                  "library/library_store/login.html")


# function to render to the details page of the selected book item.
def task_item_detail(request, taskItem_id):
    for items in TaskList:
        if items.id == taskItem_id:
            break
    return render(request,
                  "library/library_store/detail.html",
                  {"taskItem": items})


# function to perform login operations based on two user types admin and regular users
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == regular_users["username"] and password == regular_users["password"]:
        request.session['username'] = username
        request.session['role'] = 'regular'
        return redirect("library:home")
    elif username == admin_user["username"] and password == admin_user["password"]:
        request.session['username'] = username
        request.session['role'] = 'admin'
        return redirect("library:home")
    else:
        return redirect("library:home")


# function to logout from the webapp.
def logout(request):
    del request.session['username']
    del request.session['role']
    return redirect('library:home')


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


# function to render to edit an item page.
def edit_item(request, taskItem_id):
    if 'username' in request.session:
        if request.session['role'] == "admin":
            for items in TaskList:
                if items.id == taskItem_id:
                    break
            return render(request,
                          "library/library_store/editItem.html",
                          {"taskItem": items})
        else:
            return render(request,
                          "library/library_store/home.html",
                          {"completedtasks": completed_tasks, "pendingtasks": pending_task})
    else:
        return render(request,
                      "library/library_store/home.html",
                      {"completedtasks": completed_tasks, "pendingtasks": pending_task})


# function to display the edited item on the list page of the webapp.
def edit_task_item(request, taskItem_id):
    title = request.POST.get("Title")
    description = request.POST.get("description")
    assigned_by = request.POST.get("author")
    assigned_to = request.POST.get("assigned")
    category = request.POST.get("category")
    priority = request.POST.get("priority")
    for i in range(len(TaskList)):
        if TaskList[i].id == taskItem_id:
            break
    TaskList[i].title = title
    TaskList[i].description = description
    TaskList[i].assigned_by = assigned_by
    TaskList[i].assigned_to = assigned_to
    TaskList[i].category = category
    TaskList[i].priority = priority
    return task_item_list(request)


# function to render to delete an item page.
def delete_item(request, taskItem_id):
    if 'username' in request.session:
        if request.session['role'] == "admin":
            for items in TaskList:
                if items.id == taskItem_id:
                    break
            return render(request,
                          "library/library_store/deleteItem.html",
                          {"taskItem": items})
        else:
            return render(request,
                          "library/library_store/home.html",
                          {"completedtasks": completed_tasks, "pendingtasks": pending_task})
    else:
        return render(request,
                      "library/library_store/home.html",
                      {"completedtasks": completed_tasks, "pendingtasks": pending_task})


# function to perform delete operation on the specified item.
def delete_task_item(request, taskItem_id):
    confirm = request.POST.get("confirm")
    if confirm == "yes":
        for i in range(len(TaskList)):
            if TaskList[i].id == taskItem_id:
                break
        del TaskList[i]

    return task_item_list(request)
