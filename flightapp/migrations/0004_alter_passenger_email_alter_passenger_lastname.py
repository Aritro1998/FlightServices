# Generated by Django 4.0.6 on 2023-03-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0003_alter_passenger_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='lastName',
            field=models.CharField(max_length=20),
        ),
    ]
