from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib.auth.models import User

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['entity','quarter','status','assign_to']
    list_display = ['entity','activity_name','activity_type','quarter','due_date','target_date','actual_completion_date','status','assign_to','remakrs']
    # search_fields =['activity_name','entity','activity_type','quarter','month','periodicals','narations','due_date','target_date','actual_completion_date','event_modified','status','assign_to']
    list_editable = ['target_date','actual_completion_date','remakrs']


class ActivityNameAdmin(admin.ModelAdmin):
    list_filter = ['name',]
    list_per_page = 7 # No of records per page 

class EnityNameAdmin(admin.ModelAdmin):
    list_filter = ['entity_name',]
    list_per_page = 7 # No of records per page 

class ActivityTypeAdmin(admin.ModelAdmin):
    list_filter = ['type',]
    list_per_page = 7 # No of records per page 


admin.site.register(EnityName,EnityNameAdmin)
admin.site.register(ActivityName,ActivityNameAdmin)
admin.site.register(ActivityType,ActivityTypeAdmin)
admin.site.register(ActivityTracker,AuthorAdmin)


admin.site.site_header = "Nityo Finance Activity Tracker"
admin.site.site_title  =  "Nityo Finance Activity Tracker"
admin.site.index_title  =  "Nityo Finance Activity Tracker Admin"