# Generated by Django 5.1.4 on 2024-12-13 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_alter_attendance_meeting_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_on',
            field=models.DateField(default=datetime.date(2024, 12, 13)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 12, 13, 11, 57, 44, 474842)),
        ),
    ]
