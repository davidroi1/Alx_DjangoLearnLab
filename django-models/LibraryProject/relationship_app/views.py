from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Book, Library


def get_all_books(request):
    if request.method == 'GET':
        try:
            books = Book.objects.all()
            return render(request, 'relationship_app/list_books.html', {'books': books})
        except Book.DoesNotExist:
            return HttpResponse("No books found.", status=404)


class GetLibraryList(ListView):
    model = Library
    templat = 'relationship_app/library_detail.html'
    context = 'libraries'

