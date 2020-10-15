from django import forms
# from snowpenguin.django.recaptcha3 import ReCaptchaField
from contacts.models import Contact


class ContactForm(forms.ModelForm):
    """E-mail subscription form"""
    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent"})
        }