# Generated by Django 3.0.7 on 2020-06-09 09:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20200609_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='ad_id',
            field=models.UUIDField(default=uuid.uuid4, editable=FileExistsError),
        ),
    ]
