from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from . import models

from .models import Book
from .models import Library


def list_books(request):
    try:
        books = Book.objects.all()
        return render(request, 'bookshelf/list_books.html', {'books': books})
    except Book.DoesNotExist:
        return HttpResponse("No books found.", status=404)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("Registration successful.")
    form =  UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})


class LibraryDetailView(ListView):
    model = Library
    template_name = 'bookshelf/library_detail.html'
    context_object_name = 'library'


def user_passes(user):
    if user.is_authenticated:
        return True
    return False


@user_passes_test(user_passes, login_url='/login/')
def admin_view(request):
    if request.user.profiles.role == 'admin':
        return render(request, 'bookshelf/admin_view.html')
    else:
        return HttpResponse("You do not have permission to view this page.", status=403)


@user_passes_test(user_passes, login_url='/login/')
def librarian_view(request):
    if request.user.profiles.role == 'librarian':
        return render(request, 'bookshelf/librarian_view.html')
    else:
        return HttpResponse("You do not have permission to view this page.", status=403)


@user_passes_test(user_passes, login_url='/login/')
def member_view(request):
    if request.user.profiles.role == 'member':
        return render(request, 'bookshelf/member_view.html')
    else:
        return HttpResponse("You do not have permission to view this page.", status=403)
    

@permission_required('bookshelf.can_add', raise_exception=True)
def create(request, id):
    try:
        author = models.Author.objects.get(id=id).first()
        if request.method == 'POST':
            title = request.POST.get('title')
            if title and author:
                book_list = models.Book.objects.create(title=title, author=author)
                return HttpResponse("Book created successfully.")
    except HttpResponse.DoesNotExist:
            return HttpResponse("Failed to create book.", status=400)


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete(request, id):
    try:
        book_list = models.Book.objects.get(id=id)
        book_list.delete()
        return HttpResponse("Book deleted successfully.")
    except models.Book.DoesNotExist:
        return HttpResponse("Book not found.", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
    

@permission_required('bookshelf.can_edit', raise_exception=True)
def update(request, id):
    try:
        book_list = models.Book.objects.get(id=id)
        if request.method == 'POST':
            title = request.POST.get('title')
            if title:
                book_list.title = title
                book_list.save()
        return HttpResponse("Book updated successfully.")
    except models.Book.DoesNotExist:
        return HttpResponse("Book not found.", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

