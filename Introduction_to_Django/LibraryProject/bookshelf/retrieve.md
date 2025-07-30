from .models import Book

data_by_id = Book.objects.get(pk=1)
all_data = Book.objects.all()
