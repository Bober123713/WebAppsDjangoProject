from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Example URL for the home page.
    # Add more URLs for your 'base' app as needed.
]