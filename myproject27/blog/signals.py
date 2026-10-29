from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Blog

#triger whaen blog is not save
@receiver(pre_save, sender=Blog)
def before_blog_save(sender, instance, **kwargs):
    print(f"Before saving blog [pre_save]: {instance.title}")

#triger whaen blog is save
@receiver(post_save, sender=Blog)
def after_blog_save(sender, instance, created, **kwargs):
    if created:
        print(f"Blog created [post_save]: {instance.title}")
    else:
        print(f"Blog updated [post_save]: {instance.title}")

