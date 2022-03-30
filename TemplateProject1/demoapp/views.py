from django.http import HttpResponse
from django.shortcuts import render
import datetime

def template_view(request):
    dt = datetime.datetime.now()
    name = "Komal Saluja"
    address = "Nagpur"
    mobno = "9999999999"
    my_dict = {'date':dt,'nm':name,'addr':address,'Mno':mobno}
    return render(request,'demoapp/index.html',my_dict)
