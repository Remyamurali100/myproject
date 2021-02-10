from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Selecting
# from realtor.models import Realtor 
from listings.choices import price_choices, bedroom_choices, state_choices

from accounts.models import UserProfile

# Create your views here.
def index(request):
    listings = Selecting.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context ={
        'listings': listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # users=UserProfile.objects.all()
    # print(users)
    
    # # mvp_realtors=User.objects.all().filter(is_active=True)

    # context= {
    #     'realtors':users,
        
    # }


    return render(request, 'pages/about.html')
