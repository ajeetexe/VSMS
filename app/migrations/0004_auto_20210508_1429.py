# Generated by Django 3.2 on 2021-05-08 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('vehicle_owner_name', models.CharField(max_length=150)),
                ('service_request_no', models.AutoField(default=100000000, primary_key=True, serialize=False, unique=True)),
                ('service_request_date', models.DateTimeField(auto_now_add=True)),
                ('vehicle_type', models.CharField(choices=[('b', 'Bike'), ('c', 'Car'), ('s', 'Scooter')], max_length=1)),
                ('vehicle_name', models.CharField(max_length=100)),
                ('vehicle_number', models.CharField(max_length=50)),
                ('license_number', models.CharField(max_length=50)),
                ('type_of_service', models.CharField(choices=[('s', 'Service Centre'), ('h', 'Home Service')], max_length=1)),
                ('owner_address', models.TextField()),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('service_charge', models.CharField(max_length=10)),
                ('parts_charge', models.CharField(max_length=10)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
