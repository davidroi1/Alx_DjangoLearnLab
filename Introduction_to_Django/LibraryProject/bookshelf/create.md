from .models import Book


create_object = Book.objects.create(title='1984', author='George Orwell', year=1949)