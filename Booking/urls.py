from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:car_id>/', views.create_booking, name='create_booking'),
    path('book/success/', views.create_booking_success, name='create_booking_success'),
    path('download_bookings/', views.download_bookings, name='download_bookings'),
]
