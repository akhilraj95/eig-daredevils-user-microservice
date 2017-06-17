from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    superpower =  models.TextField(max_length=100, blank=True)
    xmen = models.BooleanField(default = False)
    avenger = models.BooleanField(default = False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class AccessToken(models.Model):
    user = models.ForeignKey(User)
    jwt = models.TextField(max_length=500, blank=False)


class Bio(models.Model):
	user = models.ForeignKey(User,unique = True)
	html = models.TextField(max_length=10000,blank=True)
    