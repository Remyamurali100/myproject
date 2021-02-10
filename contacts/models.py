from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import User

class Contacts(models.Model):
    listing=models.CharField(max_length=200)
    listing_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
   
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now, blank=True)
    user_id=models.IntegerField(blank=True)
    def __str__(self):
        return self.name


class ContactNotification(models.Model):
    sender = models.IntegerField(blank=True)
    receiver = models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

