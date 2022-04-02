from django.contrib import admin
from django.shortcuts import render
from demoapp.models import PuneJobs,BengaluruJobs,ChennaiJobs,HyderabadJobs

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','mobno']

class BengaluruJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','mobno']

class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','mobno']

class HyderabadJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','mobno']

admin.site.register(PuneJobs,PuneJobsAdmin)
admin.site.register(BengaluruJobs,BengaluruJobsAdmin)
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)
admin.site.register(HyderabadJobs,HyderabadJobsAdmin)
    
