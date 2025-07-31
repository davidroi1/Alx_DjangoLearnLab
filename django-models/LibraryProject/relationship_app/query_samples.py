from .models import Book, Author, Library, Librarian


def get_books_by_author(author_name):
    """Retrieve all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except (Author.DoesNotExist, Book.DoesNotExist):
        return None
    

def get_all_books_in_library(library_name):
    """retrieve all books in all libraries."""
    try:
        library =Library.objects.get(name=library_name)
        return library.books.all()
    except (Library.DoesNotExist, Book.DoesNotExist):
        return None
    

def get_librarian_by_library(library_title):
    try:
        library = Library.objects.get(title=library_title)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None