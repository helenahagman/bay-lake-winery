from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import crispy_forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message', 'subscribe_to_newsletter']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 8}),
        }