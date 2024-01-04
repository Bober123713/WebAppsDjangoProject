from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Car


def create_booking(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the user
            booking.save()
            return redirect('some_success_page')  # Redirect as necessary
    else:
        form = BookingForm(initial={'car': car})
    return render(request, 'create_booking.html', {'car': car})