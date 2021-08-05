from django import forms
from .models import  Car,User,Seller
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

# user signup from
class UserSignupForm(UserCreationForm):
    #email
    class Meta(UserCreationForm.Meta):
        model = User
    
    @ transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_user=True
        user.save()
        user=User.objects.create(user=user)
        #email
        user.save()

        # car=Car.objects.create(user=user)
        # car.interests.add(*self.cleaned_data.get('interests'))
        return user

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
