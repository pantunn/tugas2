from asyncio import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Item_todolist



@login_required(login_url='/todolist/login/')

def show_todolist(request):
    username = request.user.username
    user_id = request.user.id
    data_of_todolist = Item_todolist.objects.filter(user_id=user_id)
    context = {
        'username': username,
        'todolist' : data_of_todolist,
        
        }
    return render(request, "my_todolist.html",context)


def my_todolist(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()  
        is_finished = False
        Item_todolist.objects.create(title=title, description=description, date=date, user=request.user)
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        return response
    return render(request, "todolist.html")

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    data = Item_todolist.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:my_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/todolist/login/')
def todolist_ajax(request):
    username = request.user.username
    user_id = request.user.id
    data_of_todolist = Item_todolist.objects.filter(user_id=user_id)
    context = {
        'username': username,
        'todolist' : data_of_todolist,
        
        }
    return render(request, "my_todolist.html",context)

@login_required(login_url='/todolist/login/')
def task_delete(request, id):
    data_task = Task.objects.get(id=id)
    data_task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))