from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from .views import LibraryDetailView
from .views import list_books
from . import views


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/register.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('Admins/', views.admin_view, name='admin_view'),
    path('Librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]