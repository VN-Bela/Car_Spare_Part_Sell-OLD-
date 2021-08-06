from django import forms
from .models import  Car,User,Seller,Buyer
from django.forms.utils import ValidationError
from django.contrib.auth.forms import  UserCreationForm
from django.db import  transaction

class Car_Part_Form(forms.ModelForm):
    class Meta:
        model=Car
        fields=[
            'Car_name',
            'Car_model',
            'Car_Part_Name',
            'Car_Part_Info',
            'Car_Part_Cat',
            'Car_Part_Discription',
            'Owner_info',
        ]
# seller signup form    
class SellerSignUpFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller= True
        user.save()
        if commit:
            user.save()
        return user

# user signup from
class BuyerSignupForm(UserCreationForm):
    #email
    class Meta(UserCreationForm.Meta):
        model = User
    
    @ transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_user=True
        user.save()
        user=Buyer.objects.create(user=user)
        #email
        return user
        # car=Car.objects.create(user=user)
        # car.interests.add(*self.cleaned_data.get('interests'))