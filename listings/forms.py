from django import forms
from listings.models import Selecting
from django.utils.timezone import datetime

from django.contrib.auth.models import User

class PgaddForm(forms.ModelForm):
    class Meta:
    	model = Selecting
    	fields = ('title','address', 'city','state','zipcode' ,'description' ,'price',
    		'bedrooms' ,'bathrooms' ,'garage' ,'sqft' ,'lot_size','photo_main','photo_1',
    		'photo_2','photo_3','photo_4','photo_5','photo_6','is_published','list_date')
    	
        

    	widgets = {

    		'title': forms.TextInput(attrs={'style': 'width: 400px'}),
    		'address': forms.TextInput(attrs={'style': 'width: 400px'}),
    		'city': forms.TextInput(attrs={'style': 'width: 400px'}),
    		'state': forms.TextInput(attrs={'style': 'width: 400px'}),
    		'zipcode': forms.TextInput(attrs={'style': 'width: 400px'}),
    		'price': forms.NumberInput(attrs={'style': 'width: 400px'}),
    		'bedrooms': forms.NumberInput(attrs={'style': 'width: 400px'}),
    		'bathrooms': forms.NumberInput(attrs={'style': 'width: 400px'}),
    		'garage': forms.NumberInput(attrs={'style': 'width: 400px'}),
    		'sqft': forms.NumberInput(attrs={'style': 'width: 400px'}),
    		'lot_size': forms.NumberInput(attrs={'style': 'width: 400px'}),
    		'list_date': forms.TextInput(attrs={'style': 'width: 400px'}),
            

             
             
             
             
            }





              #   labels = {
            
#       #       'realtor':'Realtor Name',
#       #       'photo':'Photo',
#       #       'description':'Description',
#     		# 'phone':'Phone', 
#     		# 'email':'email' ,
#     		# 'is_mvp' :'is_mvp',
#     		# 'hire_date': 'hire_date',
#       #       'title':'title',
#     		# 'address':'address', 
#     		# 'city ':'city',
#    			# 'state ':'state',
#     		# 'zipcode':'zipcode', 
#     		# 'description':'description',
#     		# 'price ':'price',
#     		# 'bedrooms':'bedrooms', 
#    			# 'bathrooms':'bathrooms', 
#     		# 'garage':'garage' ,
#     		# 'sqft ':'sqft',
#     		# 'lot_size':'lot_size' ,
#     		# 'photo_main':'photo_main',
#     		# 'photo_1 ':'photo_1',
#     		# 'photo_2 ':'photo_2',
#     		# 'photo_3':'photo_3', 
#     		# 'photo_4':'photo_4', 
#     		# 'photo_5':'photo_5', 
#     		# 'photo_6':'photo_6', 
#     		# 'is_published': 'is_published',
#     		# 'list_data':'list_data' 
#       #   }

    
              # self.fields['realtor'].value="{{ user.id }}"
#         # value="{{ user.id }}"


#         self.fields['realtor'].widget.attrs['readonly'] = True
       

   