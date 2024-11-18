from django import forms
from .models import Review

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('content',)