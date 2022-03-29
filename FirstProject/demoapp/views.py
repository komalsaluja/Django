from django.http import HttpResponse
from django.shortcuts import render


def demo_view(request):
    return HttpResponse('<h1>Shri Ganesh</h1>')
