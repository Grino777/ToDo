from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    finished = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)