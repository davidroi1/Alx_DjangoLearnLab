from .models import Book

data_by_id = Book.objects.get(pk=1)

all_data = Book.objects.all()

attribute_data = Book.objects.filter(title="1984")
