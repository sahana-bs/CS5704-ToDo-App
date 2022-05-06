from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class TaskLists(models.Model):
    title = models.CharField(max_length=200)
    assigned_by = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    due_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:task-detail', args=[self.id])

#
# class EventList(models.Model):
#     img = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     date_started = models.DateTimeField(auto_now_add=True)
#     location = models.CharField(max_length=200)
#     registered = models.BooleanField(default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Reviews(models.Model):
    review = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(TaskLists, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review[:20]

    def get_absolute_url(self):
        return reverse('library:task-detail', args=[self.task_id])




