from django import forms
from django.forms import TextInput

from .models import Driver,Car

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields=["name","license",]
        labels={"name":"Driver Name","license":"License Number",}
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Driver Name'
            }),
            'license': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'License Number'
            }),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields=["make","model","year","vin","owner",]
        labels={"make":"Manufacturer Name","model":"Car Model Name","year":"Year of Manufacture","vin":"16DigitChaseyNumber","owner":"OwnerID"}
        widgets = {
            'make': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Manufacturer'
            }),
            'model': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Vehicle Model'
            }),
            'year': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'year of manufacture'
            }),
            'vin': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Vehicle Chassey Number'
            }),
        }