from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=155, verbose_name='Задание')
    description = models.TextField(verbose_name='Описание')
    status = models.BooleanField(default=False, verbose_name='Статус')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    time = models.TimeField(auto_now_add=True, verbose_name='Время добавления')