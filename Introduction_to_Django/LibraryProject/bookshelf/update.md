from .models import Book


data_info_by_id = Book.objects.get(id=1)
data_info_by_id.title = 'Nineteen Eighty-Four'