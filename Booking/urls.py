from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_booking, name='create_booking'),
]