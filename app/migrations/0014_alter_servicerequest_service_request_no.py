# Generated by Django 3.2 on 2021-05-11 07:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_servicerequest_service_request_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service_request_no',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]