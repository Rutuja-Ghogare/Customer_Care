# Generated by Django 4.0.4 on 2023-08-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer_SR',
        ),
    ]
