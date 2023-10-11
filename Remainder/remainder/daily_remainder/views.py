from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # Add additional validation and error handling here
        if not username or not password:
            return render(request, 'register.html', {'error_message': 'Please provide a username and password'})

        # Check if the username already exists
        if remainder.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Username already exists'})

        # Check for other validation conditions if needed
        if password != cpassword:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})
        else:
            r = remainder()
            r.username = username
            r.password = password
            r.cpassword = cpassword
            r.save()
            return redirect("/login/")
    return render(request, 'register.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # You can add additional validation and error handling here

        # Authenticate and login the user
        user = authenticate(request,username=username, password=password)
        print(username,password,user)
        if user:
            login(request, user)
            return redirect('profile')  # Redirect to the user's profile or another page after login

    return render(request, 'login.html')

@login_required
def profile(request):
    user = request.user

    # You can access user attributes like username, email, etc.
    username = user.username
   

    # Pass the user data to the template
    context = {
        'username': username,
    }

    return render(request, 'profile.html', context)


def home(request):
    return render(request, 'home.html')



def set_reminder(request):
    return render(request, 'set_reminder.html')

def modify_reminder(request):
    return render(request, 'modify_reminder.html')

def disable_reminder(request):
    return render(request, 'disable_reminder.html')

def delete_reminder(request):
    return render(request, 'delete_reminder.html')

def enable_reminder(request):
    return render(request, 'enable_reminder.html')

def view_reminders(request):
    return render(request, 'view_reminders.html')