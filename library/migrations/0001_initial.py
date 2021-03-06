# Generated by Django 3.2.8 on 2021-10-28 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryLists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('ratings', models.IntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
