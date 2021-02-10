from django.shortcuts import render, redirect

from django.http import HttpResponse

from notifications.models import Notification
# Create your views here.

def ShowNOtifications(request):
	user = request.user
	notifications = Notification.objects.filter(receiver=user).order_by('-date')
	Notification.objects.filter(receiver=user, is_seen=False).update(is_seen=True)

	

	context = {
		'notifications': notifications,
	}

	return render(request, 'notifications/notifications.html', context)

def DeleteNotification(request, noti_id):
	user = request.user
	Notification.objects.filter(id=noti_id, receiver=user).delete()
	return redirect('show-notifications')


def CountNotifications(request):
	count_notifications = 0
	if request.user.is_authenticated:
		count_notifications = Notification.objects.filter(receiver=request.user, is_seen=False).count()

	return {'count_notifications':count_notifications}