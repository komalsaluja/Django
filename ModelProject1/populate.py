import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject1.settings')

import django
django.setup()

from demoapp.models import *
from faker import Faker
from random import *

obj=Faker()

def populate(no):
    for i in range(no):
        feno = obj.random_int(1001,9999)
        fename = obj.name()
        fesal = obj.random_int(15000,30000)
        feaddr = obj.city()
        
        emp_record = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)
        
populate(30)