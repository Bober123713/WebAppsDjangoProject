from django.db import models
from django.conf import settings
from django.utils import timezone
from CarsManagement.models import Car  # Replace with your actual Car model import


class Booking(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        # Calculate the number of days
        delta = self.end_date - self.start_date
        num_days = delta.days

        # Calculate the price
        self.price = num_days * self.car.price_per_day

        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s booking of {self.car.make} {self.car.model}"
