from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User,auth

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`=
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model)=`=
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

class make(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

class model(models.Model):
    dealer_id = models.IntegerField
    name = models.CharField(max_length=100)
    model_type =models.CharField(max_length=100)
    year =models.DateField

class dealer(models.Model):
    dealer_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    zip=models.IntegerField()
    state=models.CharField(max_length=100)
    
class review(models.Model):
    dealer=models.ForeignKey(dealer, on_delete=models.CASCADE, related_name="reviews")
    content=models.CharField(max_length=1000,default="no comments yet")
    date_joined=models.DateTimeField(auto_now_add=True)
    name=User.first_name
    
    class Meta:
        ordering=("date_joined",)

    def  ___str___(self):
        return f"Review by {self.name}"