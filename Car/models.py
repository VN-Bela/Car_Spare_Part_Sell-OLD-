from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import  AbstractUser


# Create your models here.

Part_Category=(
    ('E','Engine'),
    ('FS','Fuel System'),
    ('EX_S','Exhaust System'),
    ('CS','Colling System'),
    ('LS','Lubrication System'),
    ('EL_S','Electrical System'),
    ('T','Transmission'),
    ('C','Chassis'),
)
Part_Info=(
    ('N',"New"),
    ('U',"USE"),
)
# User Model
class User(AbstractUser):
    is_user=models.BooleanField("User status",default=False)
    is_seller=models.BooleanField("Seller status",default=False)
    def __str__(self):
        return self.username

# Buyer Model
class Buyer(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE)

# Seller Model
class Seller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    



class Car(models.Model):    
    Car_name=models.CharField(max_length=100)
    Car_model=models.CharField(max_length=100)
    Car_Part_Name=models.CharField(max_length=100)
    Car_Part_Info=models.CharField(max_length=50,choices=Part_Info)
    Car_Part_Cat=models.CharField(max_length=50,choices=Part_Category)
    Car_Part_Discription=models.CharField(max_length=100)
    Owner_info=models.CharField(max_length=200)
    suser=models.ForeignKey(Seller,on_delete=models.CASCADE)
  

    def __str__(self):
        return self.Car_Part_Name


