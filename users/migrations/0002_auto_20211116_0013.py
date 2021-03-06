# Generated by Django 3.2.8 on 2021-11-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('not shared', 'Not Shared')], default='not shared', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='profile_pic',
            field=models.TextField(blank=True),
        ),
    ]
