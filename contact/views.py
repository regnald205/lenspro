from django.shortcuts import render,redirect
from .models import Contact_client
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        

        contact = Contact_client(name=name,email=email,phone=phone,message=message)
        contact.save()

        messages.success(request,'Your request has been submitted,we will get back to you soon')

   

   
    return redirect('index')
