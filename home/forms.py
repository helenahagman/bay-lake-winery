from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import ContactForm


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message', 'subscribe_to_newsletter']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 8}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactFormModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'message',
            'subscripe_to_newsletter',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
