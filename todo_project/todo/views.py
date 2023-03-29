from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .forms import ToDoForm
from .models import ToDo

# Create your views here.
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'todo/main.html')

    def post(self, request):
        pass

class ToDoListView(ListView):
    model = ToDo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'

class CreateToDoView(CreateView):
    model = ToDo
    form_class = ToDoForm
    template_name = 'todo/create_task.html'
    success_url = 'todo_list'
    context_object_name = 'form'

class DeleteToDoView(DeleteView):
    model = ToDo
    success_url = 'todo_list'