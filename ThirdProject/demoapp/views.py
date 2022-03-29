from django.http import HttpResponse
from django.shortcuts import render

#Single application with multiple views

def python_view(request):
    return HttpResponse('<h1>Welcome to Python World</h1>')

def django_view(request):
    return HttpResponse('<h1>Welcome to Django World</h1>')

def restAPI_view(request):
    return HttpResponse('<h1>Welcome to restAPI World</h1>')

