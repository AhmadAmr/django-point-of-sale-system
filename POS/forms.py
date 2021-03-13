from django import forms
from django.forms import ModelForm,Textarea,TextInput

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields=['phone_no','area_name','street_name','apartment_number','country','default']
        widgets = {
            'area_name': TextInput(attrs={'placeholder': 'area_name'}),
            'phone_no' : TextInput(attrs={'placeholder': '01234567899'}),
        }
        