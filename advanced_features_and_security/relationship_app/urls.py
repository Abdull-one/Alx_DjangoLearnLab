from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', auth_views.LoginView.as_view(), name='home'),  # Temporary home route
]
