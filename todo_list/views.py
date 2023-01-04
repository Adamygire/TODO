from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
    if  request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()    
            messages.success(request, ('Item Has Been Added To List!'))

    all_items = List.objects.all
    return render(request, 'home.html', { 'all_items': all_items })

def about(request):
    context =  {'first_name': 'Adam', 'last_name': 'Mohamed'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home') 

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home') 

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home') 

def edit(request, list_id):
    if  request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()    
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', { 'item': item }) 

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'from':UserCreationForm()}) 
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'singupuser.html', {'from':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'singupuser.html', {'from':UserCreationForm(), 'error':'Passwords did not match'}) 

def signin(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'from':AuthenticationForm()}) 
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currenttodos')


def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def current_todos(request):
    return render(request, 'currenttodos.html')