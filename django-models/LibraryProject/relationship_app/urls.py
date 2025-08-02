from django.urls import path
from relationship_app import views


urlpatterns = [
    path('books/', views.get_all_books, name='list_books'),
    path('libraries/', views.GetLibraryList.as_view(), name='library_list')
]