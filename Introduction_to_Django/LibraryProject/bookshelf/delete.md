from .models import Book


info_by_id = Book.objects.get(id=1)
info_by_id.delete()