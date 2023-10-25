from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Product, Category


class ProductForm(forms.ModelForm):
    image = CloudinaryFileField(
        options={
            'folder': 'PP5',
        }
    )

    class Meta:
        model = Product
        fields = '__all__'
