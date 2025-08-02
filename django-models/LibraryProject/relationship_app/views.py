from django.shortcuts import render
from .models import Author, Book, Librarian, Library
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . import query_samples


def get_all_books(request):
    if request.method == 'GET':
        try:
            books = Book.objects.all()
            return render(request, 'list_books.html', {'books': books})
        except Book.DoesNotExist:
            return HttpResponse("No books found.", status=404)


class GetLibraryList(ListView):
    model = Library
    templat = 'library_detail.html'
    context = 'libraries'

