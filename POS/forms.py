from django import forms
from django.forms import ModelForm,Textarea,TextInput

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields=['phone_no','area_name','street_name','apartment_number','default']
        widgets = {
            'area_name': TextInput(attrs={'placeholder': 'area_name'}),
            'phone_no' : TextInput(attrs={'placeholder': '01234567899'}),
        }
class SalesFiltersForm(forms.Form):
    date_from = forms.DateTimeField()
    date_to = forms.DateTimeField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date_from'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_from'].widget.attrs.update({'placeholder': 'Date from'})
        self.fields['date_to'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_to'].widget.attrs.update({'placeholder': 'Date to'})
        self.fields['date_from'].widget.attrs.update({'id': 'date_from'})
        self.fields['date_to'].widget.attrs.update({'id': 'date_to'})

