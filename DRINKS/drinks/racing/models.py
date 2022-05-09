from django.db import models

# Create your models here.


class Driver(models.Model):

    driver_name = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=100)
    rounds = models.IntegerField(default=0)

    def __str__(self):
        return self.driver_name
