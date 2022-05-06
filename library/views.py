from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import  User, Reviews, TaskLists
from actions.models import Action
from users.models import UserProfiles
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import Q


# Create your views here.
def task_item_list(request):
    task = TaskLists.objects.order_by('id').filter(pending=True)
    taskList = task.filter(assigned_to=request.session.get("username"))
    return render(request,
                  "library/library_store/list.html",
                  {"taskList": taskList})


# function to render to the home page.
def todo_home(request):
    actions = Action.objects.all().order_by('-created')
    completed = TaskLists.objects.all().filter(completed=True)
    completed_tasks = completed.filter(Q(assigned_by=request.session.get("username")) | Q(assigned_to=request.session.get("username")))
    pending = TaskLists.objects.all().filter(pending=True)
    pending_task = pending.filter(Q(assigned_by=request.session.get("username")) | Q(assigned_to=request.session.get("username")))
    return render(request,
                  "library/library_store/home.html",
                  {"completedtasks": completed_tasks, "pendingtasks": pending_task, "actions": actions})


# function to render to the details page of the selected task item.
def task_item_detail(request, taskItem_id):
    items = TaskLists.objects.get(pk=taskItem_id)
    return render(request,
                  "library/library_store/detail.html",
                  {"taskItem": items})


# function to render to Add task page.
def task_item(request):
    completed = TaskLists.objects.all().filter(completed=True)
    completed_tasks = completed.filter(
        Q(assigned_by=request.session.get("username")) | Q(assigned_to=request.session.get("username")))
    pending = TaskLists.objects.all().filter(pending=True)
    pending_task = pending.filter(
        Q(assigned_by=request.session.get("username")) | Q(assigned_to=request.session.get("username")))
    if 'username' in request.session:
            return render(request,
                          "library/library_store/addItem.html")
    else:
        return render(request,
                      "library/library_store/home.html",
                      {"completedtasks": completed_tasks, "pendingtasks": pending_task})


# function to create an entry in the lists page.
def createTaskItem(request):
    if request.method == 'POST':
        title = request.POST.get("Title")
        description = request.POST.get("description")
        assigned_by = request.POST.get("author")
        assigned_to = request.POST.get("assigned")
        category = request.POST.get("category")
        priority = request.POST.get("priority")
        due_date = request.POST.get("dueDate")
        user = User.objects.get(username=request.session.get("username"))
        taskItem = TaskLists(
            title=title,
            assigned_by=assigned_by,
            assigned_to=assigned_to,
            category=category,
            priority=priority,
            description=description,
            due_date=due_date,
            user=user)
        taskItem.save()

        # log the action
        action = Action(
            user=user,
            verb="added a new task",
            target=taskItem
        )
        action.save()

        messages.add_message(request, messages.SUCCESS,
                             "You have successfully submitted the task : %s" % taskItem.title)
        return redirect('library:task-detail', taskItem.id)
    else:
        return render(request,
                      "library/library_store/addItem.html")


# function to render to edit an item page.
def edit_item(request, taskItem_id):
    taskList = TaskLists.objects.get(pk=taskItem_id)
    completed = TaskLists.objects.all().filter(completed=True)
    completed_tasks = completed.filter(
        Q(assigned_by=request.session.get("username")) | Q(assigned_to=request.session.get("username")))
    pending = TaskLists.objects.all().filter(pending=True)
    pending_task = pending.filter(
        Q(assigned_by=request.session.get("username")) | Q(assigned_to=request.session.get("username")))
    if 'username' in request.session:
            return render(request,
                          "library/library_store/editItem.html",
                          {"taskItem": taskList})
    else:
        return render(request,
                      "library/library_store/home.html",
                      {"completedtasks": completed_tasks, "pendingtasks": pending_task})


# function to display the edited item on the list page of the webapp.
def edit_task_item(request, taskItem_id):
    taskList = TaskLists.objects.get(pk=taskItem_id)
    user = User.objects.get(username=request.session.get("username"))
    if request.method == 'POST':
        title = request.POST.get("Title")
        description = request.POST.get("description")
        assigned_by = request.POST.get("author")
        assigned_to = request.POST.get("assigned")
        category = request.POST.get("category")
        priority = request.POST.get("priority")
        due_date = request.POST.get("dueDate")

        if taskList.category != category:
            verb = "edited the task category of "
        elif taskList.description != description:
            verb = "edited the task description of "
        elif taskList.priority != priority:
            verb = "edited the task priority of "
        elif taskList.due_date != due_date:
            verb = "edited the task due date of "
        elif taskList.title != title:
            verb = "edited the title date to "
        else:
            verb = "edited the task details "

        taskList.title = title
        taskList.description = description
        taskList.assigned_by = assigned_by
        taskList.assigned_to = assigned_to
        taskList.category = category
        taskList.priority = priority
        taskList.due_date = due_date
        taskList.save()
        # log the edit action.
        action = Action(
            user=user,
            verb=verb,
            target=taskList
        )
        action.save()
        return redirect('library:task-detail', taskItem_id)
    else:
        return render(request,
                      "library/library_store/editItem.html",
                      {"bookItem": taskList})


# function to render to delete an item page.
def delete_item(request, taskItem_id):
    taskList = TaskLists.objects.get(pk=taskItem_id)
    completed = TaskLists.objects.all().filter(completed=True)
    completed_tasks = completed.filter(
        Q(assigned_by=request.session.get("username")) | Q(assigned_to=request.session.get("username")))
    pending = TaskLists.objects.all().filter(pending=True)
    pending_task = pending.filter(
        Q(assigned_by=request.session.get("username")) | Q(assigned_to=request.session.get("username")))
    if 'username' in request.session:
            return render(request,
                          "library/library_store/deleteItem.html",
                          {"taskItem": taskList})
    else:
        return render(request,
                      "library/library_store/home.html",
                      {"completedtasks": completed_tasks, "pendingtasks": pending_task})


# function to perform delete operation on the specified item.
def delete_task_item(request):
    if request.method == 'POST':
        taskItem_id = request.POST.get("id")
        confirm = request.POST.get("confirm")
        taskList = TaskLists.objects.get(pk=taskItem_id)
        user = User.objects.get(username=request.session.get("username"))
        if confirm == "yes":
            title = taskList.title
            taskList.delete()

            action = Action(
                user=user,
                verb="deleted the task:" + title,
                target=taskList
            )
            action.save()
        return redirect("library:task-list")
    else:
        return redirect("library:task-list")


# Method to mark the tasks as complete
def complete_task(request, taskItem_id):
    task = TaskLists.objects.get(pk=taskItem_id)
    task.completed = True
    task.pending = False
    task.save()
    return redirect("library:home")


# Method to add a comment
def comment(request, taskItem_id):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    reviews = []
    if is_ajax and request.method == 'POST':
        # item_id = request.POST.get('_id')
        user_comment = request.POST.get('_user_review')
        try:
            task = TaskLists.objects.get(pk=taskItem_id)
            user = User.objects.get(username=request.session.get("username"))
            review = Reviews(
                review=user_comment,
                user=user,
                task=task)
            review.save()

            # log the action
            action = Action(
                user=user,
                verb="added a new comment!",
                target=review
            )
            action.save()
            reviews.append({"id": review.id, "review": review.review, "date": naturaltime(review.created), "user": review.user.username})
            return JsonResponse({'success': 'success', 'comment': reviews}, status=200)
        except TaskLists.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid AJAX request'}, status=400)


# Method to edit a comment.
def edit_comment(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        comment_id = request.POST.get('_comment_id')
        updated_comment = request.POST.get('_new_comment')
        try:
            comment = Reviews.objects.get(pk=comment_id)
            comment.review = updated_comment
            comment.save()

            return JsonResponse({'success': 'success'}, status=200)
        except TaskLists.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid AJAX request'}, status=400)


# Method to delete a comment
def delete_comment(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        comment_id = request.POST.get('_comment_id')
        try:
            comment = Reviews.objects.get(pk=comment_id)
            comment.delete()
            return JsonResponse({'success': 'success'}, status=200)
        except TaskLists.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid AJAX request'}, status=400)


# Method to view all comments.
def view_review(request, taskItem_id):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    reviews = []

    if is_ajax and request.method == 'GET':
        try:
            if "username" in request.session:
                userID = User.objects.get(username=request.session.get("username")).id
                userRole = UserProfiles.objects.get(user_id=userID)
                role = userRole.role
            else:
                role = None
            item = Reviews.objects.filter(task_id=taskItem_id).order_by("-created")
            for i in item:
                reviews.append({"id": i.id, "review": i.review, "date": naturaltime(i.created), "user": i.user.username, "role": role})
            return JsonResponse({'success': 'success', 'review': reviews}, status=200)
        except TaskLists.DoesNotExist:
            return JsonResponse({'error': 'Item Not Found'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Request'}, status=400)





