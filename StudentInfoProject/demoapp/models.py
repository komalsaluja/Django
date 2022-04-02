from django.db import models

class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=50)
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField() # length=254
    mobno = models.IntegerField()
    address = models.TextField()
    