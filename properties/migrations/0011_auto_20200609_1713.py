# Generated by Django 3.0.7 on 2020-06-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_reserve_ads_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='ads_id',
            field=models.CharField(max_length=8),
        ),
    ]
