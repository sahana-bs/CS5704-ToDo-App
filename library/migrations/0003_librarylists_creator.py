# Generated by Django 3.2.8 on 2021-11-04 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_librarylists_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarylists',
            name='creator',
            field=models.CharField(default='admin', max_length=200),
        ),
    ]
