# Generated by Django 5.0 on 2024-01-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='transmission_type',
            field=models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], default='Automatic', max_length=10),
        ),
    ]