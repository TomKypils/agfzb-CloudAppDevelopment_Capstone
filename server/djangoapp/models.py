from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return "Name: " + self.name + "," + "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer = models.IntegerField()
    name = models.CharField(null=False, max_length=30, default='')
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon')
    ]
    type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )
    year = models.DateField()
    def __str__(self):
        return "Name: " + self.name + "," + "Type: " + self.type



# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
