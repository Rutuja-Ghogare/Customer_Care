# Generated by Django 4.0.4 on 2023-08-13 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportticket',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
