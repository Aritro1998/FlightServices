# Generated by Django 4.0.6 on 2023-03-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0002_alter_flight_estimatedtimeofdeparture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='lastName',
            field=models.CharField(max_length=50),
        ),
    ]