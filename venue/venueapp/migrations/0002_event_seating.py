# Generated by Django 4.1 on 2023-01-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("venueapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="seating",
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
    ]
