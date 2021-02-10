from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts,ContactNotification


from django.core.mail import send_mail

def contact(request):
    if request.method=='POST':
        receiver_id=request.POST['listing_id']
        print(receiver_id)
        listing =request.POST['listing']
        name =request.POST['name']
        email =request.POST['email']
        
        message =request.POST['message']
        sender_id =request.POST['user_id']
        realtor_email =request.POST['realtor_email']

        # check if user has made inquiry already

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted=Contacts.objects.all().filter(listing_id=receiver_id, user_id=sender_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+receiver_id)

        contact=Contacts(listing=listing, listing_id=receiver_id, name=name, email=email, message=message, user_id=sender_id)

        contact.save()
        contact_notification=ContactNotification(sender=sender_id,receiver=receiver_id,name=name,message=message,email=email)
        contact_notification.save()
        
                
        



        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+receiver_id)



# notifications
def ContactNotifications(request):
    user = request.user.id
    notifications = ContactNotification.objects.filter(receiver=user).order_by('-date')
    ContactNotification.objects.filter(receiver=user, is_seen=False).update(is_seen=True)

    

    context = {
        'notifications': notifications,
    }

    return render(request, 'contacts/contact_notifications.html', context)

def Delete_contact_Notification(request, noti_id):
    user = request.user.id
    ContactNotification.objects.filter(id=noti_id, receiver=user).delete()
    return redirect('contact-notifications')


def Contact_CountNotifications(request):
    contact_count_notifications = 0
    if request.user.is_authenticated:
        contact_count_notifications = ContactNotification.objects.filter(receiver=request.user.id, is_seen=False).count()

    return {'contact_count_notifications':contact_count_notifications}