# Generated by Django 3.2.8 on 2022-05-05 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklists',
            name='img',
        ),
    ]
