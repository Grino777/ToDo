# Generated by Django 4.1.7 on 2023-03-29 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 29, 6, 53, 59, 87256, tzinfo=datetime.timezone.utc), verbose_name='Время добавления'),
            preserve_default=False,
        ),
    ]
