from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.


class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(default="regular", max_length=50)
    user_gender = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('not shared', 'Not Shared')
    ]
    gender = models.CharField(max_length=50, choices=user_gender, default='not shared')
    profile_pic = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('users:profile', args=[self.user.username])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfiles.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofiles.save()
