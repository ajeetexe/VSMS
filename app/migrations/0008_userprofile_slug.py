# Generated by Django 3.2 on 2021-05-09 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210508_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
    ]