from django import forms
from django.forms.widgets import DateInput
from .models import Booking
import datetime
from django.utils import timezone


class BookingForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'min': datetime.date.today()}))
    end_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'min': datetime.date.today()}))

    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'car']

    def clean_start_date(self):
        current_time = timezone.localtime(timezone.now())
        start_date = self.cleaned_data.get('start_date')

        if start_date:
            if current_time.hour >= 0:
                min_date = current_time.date() + datetime.timedelta(days=1)
            else:
                min_date = current_time.date()

            if start_date < min_date:
                raise forms.ValidationError("The starting date cannot be earlier than tomorrow after 12 AM.")

        return start_date

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("The return date cannot be earlier than the start date.")

        return cleaned_data
