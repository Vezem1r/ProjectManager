# Generated by Django 5.0.6 on 2024-05-14 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='project.task'),
        ),
    ]
