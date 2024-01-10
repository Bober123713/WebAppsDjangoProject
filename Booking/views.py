from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .forms import BookingForm
from .models import Car


@login_required
def create_booking(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.start_date = form.cleaned_data['pickup_date']
            booking.end_date = form.cleaned_data['return_date']
            booking.car = car  # Set the car here
            booking.user = request.user  # Set the user here
            booking.save()
            return redirect('create_booking_success')  # Redirect as necessary
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {'form': form, 'car': car})


def create_booking_success(request):
    return render(request, 'create_booking_success.html')


@login_required
def download_bookings(request):
    xsl_url = staticfiles_storage.url('xsl/booking_template.xsl')
    xml_content = render_to_string('bookings.xml', {'user': request.user, 'xsl_url': xsl_url})
    response = HttpResponse(xml_content, content_type='application/xml')
    response['Content-Disposition'] = 'attachment; filename="bookings.xml"'
    return response

