from .models import Book, Author, Library, Librarian


def get_books_by_author(author_name):
    """Retrieve all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except (Author.DoesNotExist, Book.DoesNotExist):
        return None
    

def get_books_in_library():
    """retrieve all books in all libraries."""
    try:
        all_books = Book.objects.all()
        return all_books
    except Book.DoesNotExist:
        return None
    

def get_librarian_by_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None