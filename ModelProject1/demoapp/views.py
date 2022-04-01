from django.http import HttpResponse
from django.shortcuts import render
from demoapp.models import Employee

def employee_info_view(request):
    employee = Employee.objects.all()  #django-ORM
    return render(request,"demoapp/emp.html",{'emp':employee})
