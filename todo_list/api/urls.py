from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'todo_list'

urlpatterns = [
     path('todos/',
         views.TodoListView.as_view(),
         name='todo_list'),
     path('todos/<pk>',
         views.TodoDetailView.as_view(),
         name='todo_detail'),
     path('signup/',
         views.signup,
         name='todo_list'),
     path('users/',
         views.get_users,
         name='todo_list'),
     path('signin/',
         views.signin,
         name='todo_list'),
     path('changePassword/<pk>',
         views.changePassword,
         name='todo_list'),
]
