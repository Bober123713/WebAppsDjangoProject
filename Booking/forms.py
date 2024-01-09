from django import forms
from django.forms.widgets import DateInput, RadioSelect, CheckboxInput, TextInput
from .models import Booking
import datetime
from django.utils import timezone


class BookingForm(forms.ModelForm):
    pickup_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'min': datetime.date.today()}))
    return_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'min': datetime.date.today()}))
    transmission_type = forms.ChoiceField(choices=Booking.TRANSMISSION_CHOICES, widget=RadioSelect)
    gps_service = forms.BooleanField(required=False, widget=CheckboxInput, label='Add GPS service')
    additional_requests = forms.CharField(required=False, widget=TextInput(attrs={'placeholder': 'Any additional requests?'}), label='Additional Requests')

    class Meta:
        model = Booking
        fields = ['pickup_date', 'return_date', 'transmission_type', 'gps_service', 'additional_requests']

    def clean_pickup_date(self):
        pickup_date = self.cleaned_data.get('pickup_date')
        if pickup_date < datetime.date.today():
            raise forms.ValidationError("The pickup date cannot be in the past.")
        return pickup_date

    def clean(self):
        cleaned_data = super().clean()
        pickup_date = cleaned_data.get('pickup_date')
        return_date = cleaned_data.get('return_date')

        if return_date and pickup_date and return_date < pickup_date:
            self.add_error('return_date', "The return date cannot be earlier than the pickup date.")
        return cleaned_data
