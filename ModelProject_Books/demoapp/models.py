from django.db import models

class Book(models.Model):
    book_no = models.IntegerField()
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
