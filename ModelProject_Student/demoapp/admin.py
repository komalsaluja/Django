from django.contrib import admin
from demoapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no','name','marks','addr']

admin.site.register(Student,StudentAdmin)
