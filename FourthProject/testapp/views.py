from django.http import HttpResponse
from django.shortcuts import render


# Single Project with multiple Application 

def test_show(request):
    return HttpResponse("<h1>Welcome to Test Application</h1>")
