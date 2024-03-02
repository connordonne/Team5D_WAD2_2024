from django.db import models

# Create your models here.

# Table for the cuisine type, PK is auto generated.
class Cuisine(models.Model):
    cuisineId = models.AutoField(primary_key=True)
    cuisineName = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.cuisineName

# Table for the restaurant, PK is auto generated.
class restaurant(models.Model):
    restaurantId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=16)
    website = models.URLField()
    openingTime = models.TimeField()
    priceRange = models.CharField(max_length=16)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name