from django import forms
from .models import DepositProducts, DepositOptions

class DepositProductsForm(forms.ModelForm):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsForm(forms.ModelForm):
    class Meta:
        model = DepositOptions
        fields = ('intr_rate_type_nm', 'intr_rate', 'intr_rate2', 'save_trm', )
        # fields = '__all__'