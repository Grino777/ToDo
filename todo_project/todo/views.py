from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, UpdateView, DetailView
from .forms import ToDoForm, SearchForm
from .models import ToDo

# Create your views here.

def search_field(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['query']
            print(title)
            obj = ToDo.objects.filter(title__icontains=title)
            print(obj)
        return render(request, 'todo/search.html', context={'data': title,
                                                            'obj': obj})


class MainPageView(TemplateView):
    template_name = 'todo/main.html'

class ToDoListView(ListView):
    model = ToDo
    template_name = 'todo/tasks_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('status', 'title')

    def get_context_data(self, *, object_list=None, **kwargs):
        object_list = super(ToDoListView, self).get_context_data()
        object_list['finished_tasks'] = object_list['object_list'].filter(status=True)
        object_list['unfinished_tasks'] = object_list['object_list'].filter(status=False)
        return object_list

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


