from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_of_production = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='cars_images', blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} - {self.year_of_production}"
