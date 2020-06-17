# Generated by Django 3.0.7 on 2020-06-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image', models.ImageField(default='default_history.jpg', null=True, upload_to='about/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'Abouts'},
        ),
    ]
