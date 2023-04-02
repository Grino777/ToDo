from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('tasks_list', ToDoListView.as_view(), name='all_tasks'),
    path('create_task', CreateToDoView.as_view(), name='create_task'),
    path('detail_task/<int:pk>', DetailToDoView.as_view()),
    path('update_task/<int:pk>', UpdateToDoView.as_view()),
    path('delete_task/<int:pk>', DeleteToDoView.as_view()),

]