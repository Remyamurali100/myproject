from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.conf import settings
# from realtor.models import Realtor

# Create your models here.
class Selecting(models.Model):
    # realtor = models.ForeignKey(Realtor,  on_delete=models.CASCADE)
    # realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    # user_id=models.IntegerField(blank=True)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.title
    
    
    '''photo = models.ImageField(upload_to='photo/%Y/%m/%d')
   
    phone = models.CharField(max_length=20)
    email=models.EmailField( max_length = 254 )
    is_mvp = models.BooleanField(default=datetime.now, blank=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    list_data = models.DateTimeField(default=datetime.now, blank=True)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_name =models.CharField(max_length=20, blank=True)'''