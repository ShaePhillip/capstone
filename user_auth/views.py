from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
# from .forms import CustomUserCreationForm  # Updated import
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def signup(request):
    if request.method == 'POST':
        # Get user data from the POST request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
      
        if User.objects.filter(username=username).exists(): 
            return HttpResponse("User already exists")
        
        user = User.objects.create_user(username=username, password=password)
        user.first_name = username
        user.save()
    return render(request, 'user_auth/signup.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('bandsite:user_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('bandsite:home')  # Redirect to the home page after logout

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "user_auth/signup.html"