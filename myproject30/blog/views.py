from email import message
import email

from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
# def send_email(request):
#     subject = 'Test Email from subash'
#     message = 'This is a test email sent from Django'
#     from_email = 'asubash151@gmail.com'
#     recipient_list =['adhikarisubash00001@gmail.com']
#     send_mail(subject, message, from_email ,recipient_list)
#     return HttpResponse('Email sent successfully')

def send_email(request):
    subject = 'Test Email from subash'
    message= render_to_string('blog/email1.html', {
        'username': 'subash',
        'course': 'django',
    })

    email=EmailMessage(
        subject,
        message,
        "asubash151@gmail.com",
        ["adhikarisubash00001@gmail.com"]
    )
    email.content_subtype= "html"
    email.send()
    return HttpResponse('Email sent successfully')
