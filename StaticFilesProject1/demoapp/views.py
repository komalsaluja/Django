import datetime
from django.shortcuts import render

def template_view(request):
    date = datetime.datetime.now()
    x = int(date.strftime("%H"))
    msg = "Hello Dude, Good "
    if x<12:
        msg = msg+"Morning!!!"
    elif x<16:
        msg=msg+"Afternoon!!!"
    elif x<21:
        msg=msg+"Evening!!!"
    else:
        msg=msg+"night!!!"
    return render(request,'demoapp/index.html',{'message':msg,'date':date})
    
    
    