from django.shortcuts import render
from demoapp.models import Book

def books_view(request):
    book = Book.objects.all()
    return render(request,'demoapp/book.html',{'book':book})