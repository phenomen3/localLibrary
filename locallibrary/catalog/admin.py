from django.contrib import admin
from django.db import models
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# minimal registration of models

# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Language)

#Define the admin class

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','date_of_birth','date_of_death')
    #lay out
    fields=['first_name', 'last_name', ('date_of_birth','date_of_death')]

class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','display_genre')

admin.site.register(Book,BookAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter=('status','due_back')
