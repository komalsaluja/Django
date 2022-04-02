from django.shortcuts import render
from demoapp.models import Student

def index_view(request):
    student = Student.objects.all()
    return render(request,'demoapp/student.html',{'student':student})
