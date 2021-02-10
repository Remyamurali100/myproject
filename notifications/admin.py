from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'is_seen',
                    'receiver', 'sender')
    list_display_links = ('id','receiver')
    list_filter = ('id',)
    list_editable = ('is_seen',)
    search_fields = ('date', 'is_seen', 'receiver',
                     'sender')
    list_per_page = 25

admin.site.register(Notification,NotificationAdmin)
