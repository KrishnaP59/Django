from django import forms
from .models import smartphone,laptop


class laptopForm(forms.ModelForm):
    class Meta:
        model = laptop
        fields = ('type', 'price', 'status', 'launch')


class smartphoneForm(forms.ModelForm):
    class Meta:
        model = smartphone
        fields = ('type', 'price', 'status', 'launch')


