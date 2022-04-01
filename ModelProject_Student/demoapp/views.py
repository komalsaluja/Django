from django.shortcuts import render
from demoapp.models import Student

def stu_info(request):
    student = Student.objects.all()
    return render(request,'demoapp/student.html',{'student':student})
    
