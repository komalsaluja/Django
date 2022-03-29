import datetime
from django.http import HttpResponse
from django.shortcuts import render

def dateTime_view(request):
    date=datetime.datetime.now()
    s='<h1>Current Date and Time is : '+ str(date) +'</h1>'
    return HttpResponse(s)