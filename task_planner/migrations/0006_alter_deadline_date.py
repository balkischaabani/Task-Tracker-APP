# Generated by Django 5.0.1 on 2024-04-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_planner', '0005_project_deadline_alter_deadline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='date',
            field=models.DateField(),
        ),
    ]
