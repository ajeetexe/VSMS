# Generated by Django 3.2 on 2021-05-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_servicerequest_service_request_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='parts_charge',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='service_charge',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
