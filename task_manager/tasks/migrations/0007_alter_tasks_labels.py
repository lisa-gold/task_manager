# Generated by Django 5.0.2 on 2024-03-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0006_alter_tasks_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.LabelRelationTask', to='labels.labels'),
        ),
    ]
