from email import message
import html

from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string




# # Create your views here.

# def send_bulk_email(request):
#     message1= ('welcome to Django Advance', 'hello it me subash adhikari','asubash151@gmail.com',['adhikarisubash00001@gmail.com'])
#     message2= ('welcome to Django Advance 2', 'hello it me subash adhikari from pokhara','asubash151@gmail.com',['subashadk2004@gmail.com'])
#     message3= ('welcome to Django Advance', 'hello it me subash adhikari','asubash151@gmail.com',['adhikari2227subash00001@gmail.com'])
#     send_mass_mail((message1,message2,message3), fail_silently=False)
#     return HttpResponse('Email sent successfully')

def send_bulk_email(request):
    subject = 'wllcome'
    from_email = 'asubash151@gmail.com'
    recipient_list =  ["adhikarisubash00001@gmail.com", "subashadk2004@gmail"]
    html_content = render_to_string('email.html', {'name': 'Subash Adhik'})
    msg = EmailMultiAlternatives(subject, 'wellcome to my platform', from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse('Email is send')
