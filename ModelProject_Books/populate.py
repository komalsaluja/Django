import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject_Books.settings')

import django
django.setup()

from demoapp.models import *
from faker import Faker
from random import *

obj=Faker()

def populate(no):
    for i in range(no):
        fbno = obj.random_int(1001,99999)
        fTitle = obj.random_element(elements=('Java','Python','FrontEnd','BackEnd','Database','Django','Spring','Blockchain','Testing'))
        fAut = obj.name()
        book_record = Book.objects.get_or_create(book_no = fbno, book_title=fTitle,book_author=fAut)

populate(30)