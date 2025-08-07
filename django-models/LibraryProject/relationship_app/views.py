from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from .models import Book
from .models import Library


def list_books(request):
    try:
        books = Book.objects.all()
        return render(request, 'relationship_app/list_books.html', {'books': books})
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
    return render(request, 'relationship_app/register.html', {'form': form})


class LibraryDetailView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def user_passes(user):
    if user.is_authenticated:
        return True
    return False


@user_passes_test(user_passes, login_url='/login/')
def admin_view(request):
    if request.user.profiles.role == 'admin':
        return render(request, 'relationship_app/admin_dashboard.html', {})
    else:
        return HttpResponse("You do not have permission to view this page.", status=403)


@user_passes_test(user_passes, login_url='/login/')
def librarian_view(request):
    if request.user.profiles.role == 'librarian':
        return render(request, 'relationship_app/librarian_dashboard.html', {})
    else:
        return HttpResponse("You do not have permission to view this page.", status=403)


@user_passes_test(user_passes, login_url='/login/')
def member_view(request):
    if request.user:
        return HttpResponse("Welcome to the member area, {}".format(request.user.profiles.user.username))
    else:
        return HttpResponse("You do not have permission to view this page.", status=403)
    