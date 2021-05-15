# Generated by Django 3.2 on 2021-05-15 07:44

import app.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_carousel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=app.models.carousel_directory_path),
        ),
    ]
