import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject_Student.settings')

import django
django.setup()

from demoapp.models import *
from faker import Faker
from random import *

obj=Faker()

def populate(no):
    for i in range(no):
        frno = obj.random_int(1001,6999)
        fname = obj.name()
        fmarks = obj.random_int(0,100)
        faddr = obj.city()
        
        student_record = Student.objects.get_or_create(roll_no=frno, name=fname, marks=fmarks, addr=faddr)
        
populate(30)