from django.shortcuts import render
from demoapp.models import *


def index_view(request):
    return render(request,'demoapp/index.html')

def punejobs_view(request):
    pjobs = PuneJobs.objects.all()
    return render(request,'demoapp/pjobs.html',{'pjobs':pjobs})

def bengalurujobs_view(request):
    bjobs = BengaluruJobs.objects.all()
    return render(request,'demoapp/bjobs.html',{'bjobs':bjobs})

def chennaijobs_view(request):
    cjobs = ChennaiJobs.objects.all()
    return render(request,'demoapp/cjobs.html',{'cjobs':cjobs})

def hyderabadjobs_view(request):
    hjobs = HyderabadJobs.objects.all()
    return render(request,'demoapp/hjobs.html',{'hjobs':hjobs})
    