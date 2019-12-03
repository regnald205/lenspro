from django.shortcuts import render
from .models import Activity
from upload.models import Upload
from employee.models import Employee

def index(request):
    # Index.html data(videos)
    activity = Activity.objects.order_by('-Event_date')[:3]
    context = {
        'activity':activity,
    }
   
    return render(request, 'activity/index.html',context)

def about(request):
    #fetch data for about.html page(CEO_Photos and team photos)
    upload = Upload.objects.order_by('Event_date')[:1]
    employee = Employee.objects.order_by('Hire_date')[:3]
    context = {
        'upload':upload,
        'employee':employee
    }
   
    return render(request, 'activity/about.html',context)

def listings(request):
    #Iisting.html data(videos and photos)
     activity = Activity.objects.order_by('-Event_date')[:6]
     upload = Upload.objects.order_by('Event_date')
     context = {
        'activity':activity,
        'upload':upload,
    }
     return render(request,'activity/listings.html',context)   

def package(request):

    return render(request,'activity/package.html')        





