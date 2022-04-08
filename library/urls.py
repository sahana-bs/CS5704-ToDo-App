from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    # post views
    path('', views.todo_home, name='home'),
    path('tasks', views.task_item_list, name='task-list'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('loginPage', views.todo_login, name='loginPage'),
    path('<int:taskItem_id>', views.task_item_detail, name='task-detail'),
    path('addTaskItem', views.task_item, name='addtaskItem'),
    path('edit/<int:taskItem_id>', views.edit_item, name='editTaskItem'),
    path('list', views.createTaskItem, name='createTaskItem'),
    path('list/<int:taskItem_id>', views.edit_task_item, name='edit_task_item'),
    path('delete/<int:taskItem_id>', views.delete_item, name='delete_item'),
    path('list/delete/<int:taskItem_id>', views.delete_task_item, name='delete_task_item'),
]
