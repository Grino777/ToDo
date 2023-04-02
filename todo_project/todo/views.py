from django.views.generic import ListView, CreateView, DeleteView, TemplateView, UpdateView, DetailView
from .forms import ToDoForm
from .models import ToDo

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'todo/main.html'

class ToDoListView(ListView):
    model = ToDo
    template_name = 'todo/tasks_list.html'
    context_object_name = 'todos'

class CreateToDoView(CreateView):
    model = ToDo
    form_class = ToDoForm
    template_name = 'todo/create_task.html'
    success_url = 'tasks_list'
    context_object_name = 'form'

class DeleteToDoView(DeleteView):
    model = ToDo
    template_name = 'todo/confirm_deletion.html'
    success_url = '/tasks_list'
    context_object_name = 'task'

class UpdateToDoView(UpdateView):
    model = ToDo
    template_name = 'todo/create_task.html'
    success_url = '/tasks_list'
    fields = ['title', 'description', 'status']

class DetailToDoView(DetailView):
    model = ToDo
    template_name = 'todo/detail_info.html'
    context_object_name = 'task'
