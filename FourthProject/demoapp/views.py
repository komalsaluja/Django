from django.http import HttpResponse
from django.shortcuts import render


# Single Project with multiple Application 

def demo_show(request):
    return HttpResponse("<h1>Welcome to Demo Application</h1>")
