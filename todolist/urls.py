from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import my_todolist

app_name = 'todolist'

urlpatterns = [
    path('', my_todolist, name='my_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_todolist, name='show_todolist'),
]