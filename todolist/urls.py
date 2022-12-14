from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import my_todolist
from todolist.views import delete_task
from todolist.views import todolist_ajax
from todolist.views import todolist_json


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', my_todolist, name='my_todolist'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('json/', todolist_json, name='todolist_json'),
    path('add/', todolist_ajax, name='todolist_ajax')
]



