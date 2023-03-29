from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view()),
    path('todo_list', ToDoListView.as_view()),
    path('create_task', CreateToDoView.as_view()),
    path('delete_task/<int:pk>', DeleteToDoView.as_view()),

]