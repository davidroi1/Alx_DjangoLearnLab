from django.contrib import admin
from .models import Book
from .models import Librarian
from .models import Author
from .models import Library
from .models import UserProfile
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_of_birth', 'profile_photo']
    search_fields = ['email', 'date_of_birth']

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Librarian, LibrarianAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)