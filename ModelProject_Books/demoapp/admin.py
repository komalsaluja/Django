from django.contrib import admin
from demoapp.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_no','book_title','book_author']

admin.site.register(Book,BookAdmin)
