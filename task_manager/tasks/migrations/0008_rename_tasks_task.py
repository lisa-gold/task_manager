# Generated by Django 5.0.2 on 2024-03-09 15:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_rename_labels_label'),
        ('statuses', '0002_rename_statuses_status'),
        ('tasks', '0007_alter_tasks_labels'),
        ('users', '0003_rename_users_customuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]