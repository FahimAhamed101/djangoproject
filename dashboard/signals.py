from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import UserProfile

User = settings.AUTH_USER_MODEL

 #this function wake up after a User object save
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        
        UserProfile.objects.create(user=instance)