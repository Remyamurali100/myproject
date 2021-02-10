from django.urls import path
from . import views

urlpatterns = [
    path('listings', views.index, name='listings'),
    path('<int:listing_id>', views.lisitng, name='listing'),
    
    path('search', views.search, name='search'),
    path('addpg', views.realtor_form, name='addpg'),
    path('<int:id>/', views.realtor_form, name='listing_update'),
    path('pub_ads', views.published_ads, name='pub_ads'),
    
    


    # path('list',views.realtor_list,name='realtor_list'),
    path('delete/<int:id>/',views.list_delete,name='list_delete'),
]