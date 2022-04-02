from django.contrib import admin
from demoapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','rollno','name','dob','marks','email','mobno','address']

admin.site.register(Student,StudentAdmin)
