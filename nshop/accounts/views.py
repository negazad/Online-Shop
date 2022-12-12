from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, authenticate , logout
from .forms import UserCreationForm

def HomeView(request):
    return render(request, 'categories/home.html')

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect('category:home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('category:home')
    else:
        form=AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('category:home')
    else:
        return render(request, 'categories/home.html')