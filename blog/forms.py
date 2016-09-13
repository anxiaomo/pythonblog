from .models import Picture
from django import forms


class PictureForm(forms.Form):
    des = forms.CharField(max_length=100)
    file = forms.ImageField()
