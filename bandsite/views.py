from django.shortcuts import render, redirect
from bandsite.models import Song
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'bandsite/home.html')

def songs_list(request):
    # Retrieve all songs from the database
    songs_list = Song.objects.all()

    # Pass the songs_list to the template for rendering
    return render(request, 'bandsite/songs.html', {'songs_list': songs_list})

@login_required(login_url='user_auth:login')
def user_profile(request):
    return render(request, 'bandsite/user_profile.html')

