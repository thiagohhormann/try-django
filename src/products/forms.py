from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title       = forms.CharField(
                    label="Title", 
                    widget=forms.TextInput(
                        attrs={
                            "placeholder": "Product Title",
                        }
                    ))
    email       = forms.EmailField()
    description = forms.CharField(
                    required=False,
                    label ='',
                    widget=forms.Textarea(
                        attrs={
                            "placeholder": "Product Description",
                            "class": "new-class-name two",
                            "id": "myid",
                            "rows": 20,
                            "cols": 80
                        }
                    ))
    price       = forms.DecimalField(initial=199.99)

    class Meta: #metadata
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    # def clean_<my_field_name>(self, *args, **kwargs):
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "Product" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
            
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")

class RawProductForm(forms.Form):
    title       = forms.CharField(
                    label='', 
                    widget=forms.TextInput(
                        attrs={
                            "placeholder": "Product Title",
                        }
                    ))
    description = forms.CharField(
                    required=False,
                    label ='',
                    widget=forms.Textarea(
                        attrs={
                            "placeholder": "Product Description",
                            "class": "new-class-name two",
                            "id": "myid",
                            "rows": 20,
                            "cols": 80
                        }
                    ))
    price       = forms.DecimalField(initial=199.99)

