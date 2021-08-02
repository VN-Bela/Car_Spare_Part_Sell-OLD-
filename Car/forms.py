from django import forms
from .models import  Car

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




