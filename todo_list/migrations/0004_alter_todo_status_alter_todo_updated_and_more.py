# Generated by Django 4.1.4 on 2023-01-04 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_todo_status_alter_todo_updated_alter_user_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('NotStarted', 'NotStarted'), ('OnGoing', 'OnGoing'), ('Completed', 'Completed')], default='NotStarted', max_length=10),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 4, 19, 55, 11, 215744, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 4, 19, 55, 11, 215218, tzinfo=datetime.timezone.utc)),
        ),
    ]