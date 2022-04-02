import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','StudentInfoProject.settings')
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
        frollno = obj.random_int(min=1001,max=2000)
        fname = obj.name()
        fdob = obj.date()
        fmarks = obj.random_int(min=1,max=100)
        femail = obj.email()
        fmobno = mobno_gen()
        faddress = obj.address()
        student_record = Student.objects.get_or_create(rollno=frollno, name = fname, dob = fdob, marks = fmarks, email = femail, mobno = fmobno, address = faddress)
        
populate(30)
        
    

    