# Generated by Django 3.0.7 on 2020-06-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='ads_id',
            field=models.CharField(default='null', max_length=8),
        ),
    ]
