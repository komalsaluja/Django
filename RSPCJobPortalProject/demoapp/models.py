from django.db import models

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    mobno = models.IntegerField()

class BengaluruJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    mobno = models.IntegerField()

class ChennaiJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    mobno = models.IntegerField()

class HyderabadJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    mobno = models.IntegerField()
