from .models import Book


create_object = Book(title='1984', author='George Orwell', year=1949)
create_object.save()