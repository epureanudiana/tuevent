# Generated by Django 2.0 on 2018-01-14 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_event_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='position',
        ),
    ]
