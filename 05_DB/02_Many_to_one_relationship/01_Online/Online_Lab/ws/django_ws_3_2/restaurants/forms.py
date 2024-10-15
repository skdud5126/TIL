from django import forms
from .models import Restaurant

class CreateRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

    