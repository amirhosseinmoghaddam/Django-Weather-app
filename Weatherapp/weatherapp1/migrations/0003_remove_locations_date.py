# Generated by Django 4.0.4 on 2022-05-23 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp1', '0002_locations_date_alter_locations_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='date',
        ),
    ]
