# Generated by Django 4.0.4 on 2023-08-13 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gas_service_app', '0007_alter_customer_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('Submitted', 'Submitted'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Submitted', max_length=20)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gas_service_app.customer')),
            ],
        ),
    ]
