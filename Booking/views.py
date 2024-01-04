from django.shortcuts import render, redirect
from .forms import BookingForm

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the user
            booking.save()
            return redirect('some_success_page')  # Redirect as necessary
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})