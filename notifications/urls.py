from django.urls import path
from .import views

urlpatterns = [
   	path('', views.ShowNOtifications, name='show-notifications'),
   	path('<noti_id>/delete', views.DeleteNotification, name='delete-notification'),
    


]