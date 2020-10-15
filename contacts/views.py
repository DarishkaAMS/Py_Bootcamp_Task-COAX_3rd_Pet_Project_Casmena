from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse

from contacts.models import Contact
from contacts.forms import ContactForm


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('home')

