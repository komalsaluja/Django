from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=50)
    marks = models.IntegerField()
    addr = models.CharField(max_length=50)

