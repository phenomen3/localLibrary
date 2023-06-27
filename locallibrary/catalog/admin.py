from django.contrib import admin
from django.db import models
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Language)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)

#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class BookInstanceAdmin:
    pass
