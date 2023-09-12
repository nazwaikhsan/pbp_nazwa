from django import forms
from .models import Item

class dataBarang(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'amount', 'description']