from django.shortcuts import render,redirect
from .models import info
from django.core.mail import send_mail
from django.conf import settings
def send_message(request):
   
    if request.method=='POST':
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']
        send_mail(
        subject,
         message,
         email,
        [settings.RECIPIENT_ADDRESS])
        return redirect('/contact/success')
    
    return render(request,'contact.html',{})
def sucessful(request):
    return render(request,'Send_success.html')