from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Book
from .models import Library


def list_books(request):
    try:
        books = Book.objects.all()
        return render(request, 'relationship_app/list_books.html', {'books': books})
    except Book.DoesNotExist:
        return HttpResponse("No books found.", status=404)


class LibraryDetailView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')
