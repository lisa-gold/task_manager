# Generated by Django 5.0.2 on 2024-03-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0005_labelrelationtask_tasks_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, null=True, through='tasks.LabelRelationTask', to='labels.labels'),
        ),
    ]
