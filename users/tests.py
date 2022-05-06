from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfiles, User

# Create your tests here.
class UserModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

    def test_string_representation(self):
        user = User(username='regular')
        self.assertEqual(str(user), user.username)

    def test_user_get_absolute_url(self):
        user = User.objects.get(username="testuser")
        UserProf = UserProfiles.objects.get(user_id=user.id)
        self.assertEqual(UserProf.get_absolute_url(), '/users/profile/testuser')

    def test_user_content(self):
        self.assertEqual(f'{self.user.username}', 'testuser')
        self.assertEqual(f'{self.user.email}', 'test@email.com')


