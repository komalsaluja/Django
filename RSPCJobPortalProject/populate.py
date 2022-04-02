import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','RSPCJobPortalProject.settings')
django.setup()

from demoapp.models import *
from faker import Faker
from random import *

obj = Faker()

def mobno_gen():
    x = randint(7,9)
    num = str(x)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

def populate(no):
    for i in range(no):
        fdate = obj.date()
        fcompany = obj.company()
        ftitle = obj.random_element(elements = ('Project Manager','Team Lead','Software Developer','DBA','UI Designer','QA Analyst'))
        feligibility = obj.random_element(elements = ('M.Tech','B.Tech','MCA','BCA'))
        faddress = obj.address()
        femail = obj.email()        
        fmobno = mobno_gen()
        
        # punejobs_record = PuneJobs.objects.get_or_create(date = fdate, company=fcompany ,title=ftitle, eligibility = feligibility ,address = faddress, email = femail, mobno = fmobno)
        # bengalurujobs_record = BengaluruJobs.objects.get_or_create(date = fdate, company=fcompany ,title=ftitle, eligibility = feligibility ,address = faddress, email = femail, mobno = fmobno)
        # chennaijobs_record = ChennaiJobs.objects.get_or_create(date = fdate, company=fcompany ,title=ftitle, eligibility = feligibility ,address = faddress, email = femail, mobno = fmobno)
        hyderabadjobs_record = HyderabadJobs.objects.get_or_create(date = fdate, company=fcompany ,title=ftitle, eligibility = feligibility ,address = faddress, email = femail, mobno = fmobno)
        
        
populate(50)

    
    