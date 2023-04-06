from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'description']
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length=155)

