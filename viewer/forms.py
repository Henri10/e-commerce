from django import forms
from .models import Smartphone

class Smartphone_form(forms.ModelForm):
    class Meta:
        model = Smartphone
        exclude = ["id", ]

    title = forms.CharField(max_length=100)
    price = forms.IntegerField()
    description = forms.Textarea()
    stock = forms.IntegerField()
    image_of_product = forms.ImageField()
