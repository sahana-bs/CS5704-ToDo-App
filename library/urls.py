from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    # post views
    path('', views.todo_home, name='home'),
    path('tasks', views.task_item_list, name='task-list'),
    path('<int:taskItem_id>', views.task_item_detail, name='task-detail'),
    path('addTaskItem', views.task_item, name='addtaskItem'),
    path('edit/<int:taskItem_id>', views.edit_item, name='editTaskItem'),
    path('list', views.createTaskItem, name='createTaskItem'),
    path('list/<int:taskItem_id>', views.edit_task_item, name='edit_task_item'),
    path('delete/<int:taskItem_id>', views.delete_item, name='delete_item'),
    path('list/delete', views.delete_task_item, name='delete_task_item'),
    path('review/<int:taskItem_id>', views.comment, name='new-review'),
    path('view/review/<int:taskItem_id>', views.view_review, name='view-review'),
    path('complete/<int:taskItem_id>', views.complete_task, name='complete_task'),
    path('edit/comment', views.edit_comment, name='edit-comment'),
    path('delete/comment', views.delete_comment, name='delete-comment'),
]
