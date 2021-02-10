from django.urls import path
from . import views

urlpatterns = [
    path('logins', views.logins, name='logins'),
    path('register/', views.register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),
    path('logout', views.logout, name='logout'),
    path('edit', views.edituserinfo, name='edit'),
    path('<int:rid>', views.userads, name='userads'),
    path('<int:cid>/', views.sample_ajax_view, name='contactinfo'),
    path('changepassword/', views.PasswordChange, name='change_password'),
   	path('dashboard', views.dashboard, name='dashboard'),
    


]