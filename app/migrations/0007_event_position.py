# Generated by Django 2.0 on 2018-01-14 16:29

from django.db import migrations
import django.utils.timezone
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_event_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='position',
            field=geoposition.fields.GeopositionField(default=django.utils.timezone.now, max_length=42),
            preserve_default=False,
        ),
    ]
