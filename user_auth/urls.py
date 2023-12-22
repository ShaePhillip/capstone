from django.urls import path
from .views import signup, user_login, user_logout
from .views import SignUpView

app_name = "user_auth"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]