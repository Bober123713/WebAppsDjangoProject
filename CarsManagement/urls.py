from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list, name='cars_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    # Add other URL patterns for this app
]
