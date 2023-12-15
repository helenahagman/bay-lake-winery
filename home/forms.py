from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
