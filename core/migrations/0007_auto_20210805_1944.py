# Generated by Django 2.1.7 on 2021-08-05 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210805_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 5, 19, 44, 40, 163662)),
        ),
    ]
