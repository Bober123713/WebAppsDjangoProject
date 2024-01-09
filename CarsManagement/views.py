from django.shortcuts import render, get_object_or_404
from .models import Car


def cars_list(request):
    # Fetch all cars from the database
    cars = Car.objects.all().order_by('make', 'model', 'year_of_production', 'price_per_day')

    # Additional processing can be done here if needed

    # Send the processed data to the template
    return render(request, 'cars_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car_detail.html', {'car': car})