from .models import Book


all_data = Book.objects.all()
data_by_id = Book.objects.get(pk=1)
