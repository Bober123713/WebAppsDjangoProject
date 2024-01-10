from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year_of_production', 'price_per_day')  # Columns to display
    list_filter = ('make', 'year_of_production')  # Filters on the sidebar
    search_fields = ('make', 'model', 'year_of_production')  # Fields to search
    ordering = ('make', 'model', 'year_of_production')  # Default sorting


admin.site.register(Car, CarAdmin)
