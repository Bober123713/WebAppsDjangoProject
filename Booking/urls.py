from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:car_id>/', views.create_booking, name='create_booking'),
]