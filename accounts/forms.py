from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
        widgets = {
             'first_name': forms.TextInput(attrs={'style': 'width: 500px'}),
             'last_name': forms.TextInput(attrs={'style': 'width: 500px'}),
             'email': forms.TextInput(attrs={'style': 'width: 500px'}),
             
            }  


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = ('photo','phone','about'  )
        widgets = {
             
             
             'phone': forms.NumberInput(attrs={'style': 'width: 350px'}),
             
            }


class ChangePasswordForm(forms.ModelForm):
    # id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 200px'}),  required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 200px'}),  required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 200px'}),  required=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'confirm_password')
    
       

