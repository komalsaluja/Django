"""FifthProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    
    path('d1/',views.display1_view),
    path('d2/',views.display2_view),
    path('d3/',views.display3_view),
    path('d4/',views.display4_view),
    path('d5/',views.display5_view),
    
]

# Now include (link) all the urls at project level