from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile
from .views import index  

urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
