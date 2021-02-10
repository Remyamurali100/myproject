from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
	user=models.OneToOneField(User ,on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='photo/%Y/%m/%d',blank=True)
	about = models.TextField(blank=True)
	phone = models.CharField(max_length=20)
	
	
	def __str__(self):
		return self.user.username


       