from django.test import TestCase
from .models import TaskLists
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.task = TaskLists.objects.create(
            title = 'A good title',
            assigned_by = "disha",
            assigned_to = "sahana",
            category = "SE Project",
            priority = "high",
            description = "Good description",
            date_created = "2022-05-04 00:52:25.829765-04",
            completed = "True",
            pending = "False",
            user = self.user
        )

    def test_string_representation(self):
        task = TaskLists(title='A sample title')
        self.assertEqual(str(task), task.title)

    def test_task_content(self):
        self.assertEqual(f'{self.task.title}', 'A good title')
        self.assertEqual(f'{self.task.user}', 'testuser')
        self.assertEqual(f'{self.task.priority}', 'high')
        self.assertEqual(f'{self.task.category}', 'SE Project')
        self.assertEqual(f'{self.task.description}', 'Good description')
        self.assertEqual(f'{self.task.assigned_by}', 'disha')
        self.assertEqual(f'{self.task.assigned_to}', 'sahana')

    def test_task_home_view(self):
        response = self.client.get(reverse('library:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/library_store/home.html')

    def test_get_absolute_url(self):
        task = TaskLists.objects.get(id=1)
        self.assertEqual(task.get_absolute_url(), '/todo/1')

