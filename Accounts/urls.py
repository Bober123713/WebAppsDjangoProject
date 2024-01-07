from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]