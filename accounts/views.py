from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts
from accounts.models import UserProfile
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse

# from .models import Listing

from notifications.models import Notification
from listings.models import Selecting
from django.http import HttpResponse

from django.contrib.auth import login, authenticate

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

# from accounts.forms import UserForm
from accounts.forms import UserProfileForm,UserUpdateForm,ChangePasswordForm




def register(request):
    if request.method =='POST':
        pform=UserProfileForm(data=request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        mymail = request.POST['email']
        
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match 
        if password==password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=mymail).exists():
                    messages.error(request,'That email is being used')
                    return redirect('register')
                else:
                    
                    if pform.is_valid():
                        user = User.objects.create_user(username=username, password=password, email=mymail, first_name=first_name, last_name=last_name)
                        user.is_active = False
                        user.save()
                    
                        profile=pform.save(commit=False)
                        profile.user=user
                        profile.save()
                    else:
                        print(pform.errors)
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your Pg account.'
                    message = render_to_string('accounts/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                    'token':account_activation_token.make_token(user),
                    })
                    to_email = mymail
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()
                    messages.success(request,'Please confirm your email address to complete the registration')
                    return redirect('logins')







                    # messages.success(request,'You are now registered and can log in')
                    # return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        pform=UserProfileForm()
        return render(request,'accounts/register.html',{'pform':pform})






def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
       
        messages.success(request,'Thank you for your email confirmation. Now you can login your account.')
        return redirect('logins')
    else:
        return HttpResponse('Activation link is invalid!')






def logins(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('logins')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

def dashboard(request):
    user_contacts= Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context ={
        'contacts':user_contacts
    }
    return render(request,'accounts/dashboard.html',context)

def edituserinfo(request):
    if request.method == 'POST':
        p_form = UserProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            
            user=u_form.save()
            
            profile=p_form.save(commit=False)
            profile.user=user
            profile.save()
        return redirect('/accounts/dashboard')
    else:
        p_form = UserProfileForm(instance=request.user.userprofile)
        u_form = UserUpdateForm(instance=request.user)

        context={'p_form': p_form, 'u_form': u_form}
        return render(request, 'accounts/userupdate.html',context )


# other user view
def userads(request,rid):
  userads = Selecting.objects.order_by('-list_date').filter(user_id_id=rid)
  # userdetails = Realtor.objects.order_by('-hire_date').filter(user_id=rid)
 
  userdetails=UserProfile.objects.get(pk=rid)
  
  paginator = Paginator(userads, 3)
  page = request.GET.get('page')
  paged_ads = paginator.get_page(page)
  context = {
        'userads': paged_ads,
        'userdetails':userdetails,
        
       
    }
  return render(request, 'accounts/user_dashboard.html', context)




def sample_ajax_view(request,cid):
    
    print(cid)
    print(request.user)
    id=request.user
    currentuser=request.user.id

    if currentuser==cid:
        print("sameuser")

       
        pass
    else:
        print("differentuser")
        different=Notification.objects.order_by('-date').filter(sender=request.user.id).filter(receiver_id=cid)
        if different:
            print("tablilund")
            pass
        else:
            print("add cheythu")
            msg=Notification(sender=request.user, receiver_id=cid)
            msg.save()



    realtor = UserProfile.objects.all().values('phone').filter(user =cid) 

    data = list(realtor)
    
    return JsonResponse(data,safe=False)


def PasswordChange(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')

            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')
            id=request.user.id
            password = User.objects.get(pk=id)
            print(password)
            if not password.check_password(old_password):
                 messages.error(request,'old password does not match')
            else:
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Password change.'
                    message = "your password changed successfully"
                    to_email = request.user.email
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()
                    messages.success(request,'password saved')

                    # if new_password != confirm_password:
                    # messages.success(request,'password does not match')
                else:
                    messages.error(request,'password does not match')
           




            
            # update_session_auth_hash(request, user)
            return redirect('change_password')
    else:
        form = ChangePasswordForm()

    context = {
        'form':form,
    }

    return render(request, 'accounts/change_password.html', context)


