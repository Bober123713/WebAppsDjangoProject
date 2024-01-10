from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'transmission_type', 'price', 'gps_service')
    list_filter = ('start_date', 'end_date', 'car', 'transmission_type', 'gps_service')
    search_fields = ('user__username', 'car__make', 'car__model', 'transmission_type')
    ordering = ('start_date', 'end_date', 'user', 'car')


admin.site.register(Booking, BookingAdmin)
