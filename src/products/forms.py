from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta: #metadata
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]