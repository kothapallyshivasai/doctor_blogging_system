# Generated by Django 5.0.3 on 2024-08-07 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_status',
            field=models.CharField(default='Not Seen', max_length=20),
        ),
    ]
