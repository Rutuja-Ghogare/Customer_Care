# Generated by Django 4.0.4 on 2023-10-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_service_app', '0024_alter_servicerequest_request_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='request_type',
            field=models.CharField(choices=[('Cylinder did not arrived', 'Cylinder did not arrived'), ('Billing Related', 'Billing Related'), ('Others', 'Others')], max_length=100),
        ),
    ]
