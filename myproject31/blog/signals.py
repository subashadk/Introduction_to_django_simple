from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)

def send_wellcome_email(sender,instance,created,**kwargs):
    if created:
        print(f"User Created : {instance.username}")

        subject = 'wllcome email'
        message = f'Welcome to our website {instance.username}'
        from_email="subash151@gmail.com"
        recipient_list = [instance.email]

        send_mail( subject, message, from_email, recipient_list, fail_silently=False )
        print("Email Sent")



