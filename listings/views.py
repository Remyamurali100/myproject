from django.shortcuts import get_object_or_404, render
from listings.models import Selecting
from django.shortcuts import redirect
# from realtor.models import Realtor
from accounts.models import UserProfile
from django.contrib.auth.models import User
from listings.forms import PgaddForm

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices


# Create your views here.


def index(request):
    listings = Selecting.objects.order_by('-list_date').filter(is_published=True)
  

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
       
    }
    return render(request, 'listings/listings.html', context)


def lisitng(request, listing_id):
    listing=get_object_or_404(Selecting, pk=listing_id)
    userdata=UserProfile.objects.get(pk=listing.user_id.id)
    
    context={
        'listing':listing,
        'userdata':userdata
        
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list=Selecting.objects.order_by('-list_date')
   
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
            
   #City
    if 'city' in request.GET:
        city = request.GET['city']
        print(city)
        if city:
            queryset_list=queryset_list.filter(city__iexact = city)

     #State
    if 'state' in request.GET:
        state = request.GET['state']
        print(state)
        if state:
            queryset_list=queryset_list.filter(state__iexact = state)
            print(queryset_list)
    
    
     # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms)
        
     # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)
                
    context={
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET,
        
    }

    return render(request, 'listings/search.html', context)





def realtor_form(request, id=0):
    if request.method == "GET":
        form = PgaddForm()
        if id == 0:
            form = PgaddForm()
            context={
            'form':form,
            
            }
            return render(request, "listings/listing_form.html",context)

        else:
            
            selection = Selecting.objects.get(pk=id) # this will select datafrom database 
            form = PgaddForm(instance=selection)
            return render(request, "listings/update_form.html",{'form':form})

    else:
        if id == 0:
            form = PgaddForm(request.POST or None, request.FILES or None)
        else:
            selection = Selecting.objects.get(pk=id)
            form = PgaddForm(request.POST or None, request.FILES or None,instance= selection)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
        return redirect('/listings/pub_ads') 




def list_delete(request,id):
    selection = Selecting.objects.get(pk=id)
    selection.delete()
    return redirect('/listings/pub_ads')

def published_ads(request):
  ads = Selecting.objects.order_by('-list_date').filter(user_id_id=request.user.id)
  paginator = Paginator(ads, 3)
  page = request.GET.get('page')
  paged_ads = paginator.get_page(page)
  context = {
        'ads': paged_ads,
       
    }
  return render(request, 'listings/realtor_ads.html', context)

