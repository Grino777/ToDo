# Generated by Django 4.1.7 on 2023-03-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Задание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
    ]
