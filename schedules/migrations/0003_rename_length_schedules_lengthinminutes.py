# Generated by Django 4.0.1 on 2022-02-26 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "schedules",
            "0002_rename_appointment_dayandtime_schedules_starttime_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="schedules",
            old_name="length",
            new_name="LengthInMinutes",
        ),
    ]