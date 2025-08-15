from django.views.generic.list import ListView
from .models import Library


class ExampleForm(ListView):
    model = Library
    template_name = 'bookshelf/form_example.html'
    context_object_name = 'libraries'