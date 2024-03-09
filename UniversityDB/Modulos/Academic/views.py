from django.shortcuts import render
from decouple import config
from django.core.mail import send_mail

# Create your views here.
# Modulos/Academic/views.py
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("¡Hola desde la aplicación Academic!")

def contactform(requets):
    return render(requets, 'contactform.html')

def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message'] + "/ Email: " + request.POST['email']
        email_from = config('EMAIL_HOST_USER')
        email_for = [config('EMAIL_HOST_USER')]
        send_mail(subject,message,email_from,email_for, fail_silently=False)
        return render(request, 'contactformsuccess.html')
    else:
        return render(request, 'contactform.html')   
    