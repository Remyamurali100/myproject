from django.urls import path

from .import views

urlpatterns=[
    path('contact', views.contact, name='contact'),
    path('', views.ContactNotifications, name='contact-notifications'),
   	path('<noti_id>/delete', views.Delete_contact_Notification, name='delete-contact-notification'),
    
]