from django.urls import path
from .views import home, songs_list, user_profile


app_name = 'bandsite'
urlpatterns = [
    path('', home, name='home'),
    path('songs/', songs_list, name='songs'),
    path('profile/', user_profile, name='user_profile'),
]
