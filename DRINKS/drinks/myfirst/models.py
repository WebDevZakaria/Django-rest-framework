from django.db import models

# Create your models here.


class Car(models.Model):
    car_name = models.CharField(max_length=200)
    desc = models.TextField(max_length=500)

    def __str__(self):

        return self.car_name


class CarSpecs(models.Model):

    car_brand = models.CharField(max_length=50)
    Car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car_brand


class Zakaria(models.Model):

    zaki_brand = models.CharField(max_length=50)

    zaki_model = models.CharField(max_length=100)

    productions_year = models.CharField(max_length=10)

    zaki_body = models.CharField(max_length=100)

    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.zaki_brand
