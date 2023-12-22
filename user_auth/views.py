from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

def signup(request):
    """
    Handle user registration.

    If the HTTP method is POST, attempt to create a new user based on the provided
    username, email, and password. Check if the username already exists. If the
    registration is successful, redirect to the signup page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response for the signup page.
    """
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
    """
    Handle user login.

    If the HTTP method is POST, validate the user login form. If the form is valid,
    log in the user and redirect to the user profile page. If the form is not valid,
    render the login page with error messages.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response for the login page.
    """
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
    """
    Handle user logout.

    Log out the currently authenticated user and redirect to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirect to the home page after logout.
    """
    logout(request)
    return redirect('bandsite:home')  # Redirect to the home page after logout

class SignUpView(generic.CreateView):
    """
    Handle user registration using Django's generic CreateView.

    Attributes:
        form_class (UserCreationForm): The form class for user registration.
        success_url (str): The URL to redirect to after successful registration.
        template_name (str): The name of the template to render for registration.

    Note:
        Inherits from Django's generic CreateView to simplify user registration.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "user_auth/signup.html"
