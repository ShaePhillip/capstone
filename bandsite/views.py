from django.shortcuts import render, redirect
from bandsite.models import Song
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Render the home page.

    Returns:
        HttpResponse: Rendered home page containing information about the band.
    """
    return render(request, 'bandsite/home.html')

def songs_list(request):
    """
    Display a list of songs grouped by album.

    Returns:
        HttpResponse: Rendered page showing a list of songs grouped by album.
    """
    songs_list = Song.objects.all()

    # Pass the songs_list to the template for rendering
    return render(request, 'bandsite/songs.html', {'songs_list': songs_list})

@login_required(login_url='user_auth:login')
def user_profile(request):
    """
    Render the user profile page for authenticated users.

    This view requires users to be logged in. If the user is not authenticated,
    they will be redirected to the login page.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: Rendered user profile page for authenticated users.
    """
    return render(request, 'bandsite/user_profile.html')

