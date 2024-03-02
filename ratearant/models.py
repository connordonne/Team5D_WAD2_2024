from django.db import models
# Create your models here.

# Table for the cuisine type.
class Cuisine(models.Model):
    cuisineId = models.AutoField(primary_key=True)
    cuisineName = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.cuisineName


# Table for the restaurant.
class Restaurant(models.Model):
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


# Table for the user.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)

    def __str__(self):
        return self.username
