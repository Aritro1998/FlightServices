# Generated by Django 4.0.6 on 2023-03-13 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0004_alter_passenger_email_alter_passenger_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightapp.flight'),
        ),
    ]