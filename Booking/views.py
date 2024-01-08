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
            booking.start_date = form.cleaned_data['pickup_date']
            booking.end_date = form.cleaned_data['return_date']
            booking.car = car
            booking.save()
            return redirect('create_booking_success')  # Redirect as necessary
    else:
        form = BookingForm(initial={'car': car})
    return render(request, 'create_booking.html', {'car': car, 'form': form})


def create_booking_success(request):
    return render(request, 'create_booking_success.html')
