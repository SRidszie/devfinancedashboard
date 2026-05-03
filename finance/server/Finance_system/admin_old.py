from dataclasses import fields
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
# from import_export.admin import DEFAULT_FORMATS
from import_export.fields import Field
from import_export import resources
from django.utils.translation import gettext as _
from django.contrib import messages
from import_export.widgets import ForeignKeyWidget
import datetime

# Register your models here.
from .models import *

admin.site.register(User)
# @admin.register(User)
# class UserAdmin(ImportExportModelAdmin):
#     pass

@admin.register(EnityName)
class EnityNameAdmin(ImportExportModelAdmin):
    list_filter = ['entity_name',]
    list_per_page = 7 # No of records per page 
    # def get_import_formats(self):
    #     """
    #     Return available import formats.
    #     """
    #     formats = DEFAULT_FORMATS[:1]
    #     return [f for f in formats if f().can_import()]

    # def get_export_formats(self):
    #     """
    #     Return available import formats.
    #     """
    #     formats = DEFAULT_FORMATS[:1]
    #     return [f for f in formats if f().can_export()]
    # pass

@admin.register(ActivityName)
class ActivityNameAdmin(ImportExportModelAdmin):
    list_filter = ['name',]
    list_per_page = 7 # No of records per page
    # def get_import_formats(self):
    #     """
    #     Return available import formats.
    #     """
    #     formats = DEFAULT_FORMATS[:1]
    #     return [f for f in formats if f().can_import()]

    # def get_export_formats(self):
    #     """
    #     Return available import formats.
    #     """
    #     formats = DEFAULT_FORMATS[:1]
    #     return [f for f in formats if f().can_export()]
    # pass

@admin.register(ActivityType)
class ActivityTypeAdmin(ImportExportModelAdmin):
    list_filter = ['type',]
    list_per_page = 7
    # def get_import_formats(self):
    #     """
    #     Return available import formats.
    #     """
    #     formats = DEFAULT_FORMATS[:1]
    #     return [f for f in formats if f().can_import()] # No of records per page 

    # def get_export_formats(self):
    #     """
    #     Return available import formats.
    #     """
    #     formats = DEFAULT_FORMATS[:1]
    #     return [f for f in formats if f().can_export()]
    # pass

class ActivityTrackerResource(resources.ModelResource):
    # entity = Field(column_name='entity',
    #     attribute='entity',
    #     widget = ForeignKeyWidget(EnityName,'entity_name'))
    # activity_name = Field(column_name='activity_name',
    #     attribute='activity_name',
    #     widget = ForeignKeyWidget(ActivityName,'name'))
    # activity_type = Field(column_name = 'activity_type',
    #     attribute='activity_type',
    #     widget = ForeignKeyWidget(ActivityType,'type'))
    # month = Field(
    #     attribute='get_month_display',
    #     column_name = _(u'month')
    # )
    # assign_to = Field(
    #     column_name = 'assign_to',
    #     attribute='assign_to',
    #     widget = ForeignKeyWidget(User,'email')
    # )
    entity = Field(column_name='entity',
        attribute='entity',
        widget=ForeignKeyWidget(EnityName, 'entity_name'))
    activity_name = Field(column_name='activity_name',
        attribute='activity_name',
        widget=ForeignKeyWidget(ActivityName, 'name'))
    activity_type = Field(column_name='activity_type',
        attribute='activity_type',
        widget=ForeignKeyWidget(ActivityType, 'type'))
    assign_to = Field(column_name='assign_to',
        attribute='assign_to',
        widget=ForeignKeyWidget(User, 'email'))
    month = Field(
        attribute='get_month_display',
        column_name=_(u'month')
    )
    class Meta:
        model=ActivityTracker
        fields = (
            'entity',
            'activity_name',
            'activity_type',
            'quarter',
            'month',
            'periodicals',
            'narations',
            'due_date',
            'target_date',
            'actual_date',
            'event_modified',
            'status',
            'assign_to',
            'remarks'
        )
    #     exclude = ('id',)
    # def dehydrate_id(self,ActivityTracker):
    #     return '%s' % (ActivityTracker.id)

    # def dehydrate_entity(self,ActivityTracker):
    #     return '%s' % (ActivityTracker.entity.entity_name)

    # def dehydrate_activity_name(self,ActivityTracker):
    #     return '%s' % (ActivityTracker.activity_name.name)

    # def dehydrate_activity_type(self,ActivityTracker):
    #     return '%s' % (ActivityTracker.activity_type.type)

    # def dehydrate_assign_to(self,ActivityTracker):
    #     return '%s' % (ActivityTracker.assign_to.email) 


@admin.register(ActivityTracker)
class ActivityTrackerAdmin(ImportExportModelAdmin):
    resource_class = ActivityTrackerResource
    list_filter = ['entity','quarter','status','assign_to']
    # list_display = ['entity','activity_name','activity_type','quarter','due_date','target_date','actual_date','status','assign_to','remarks']
    # search_fields =['activity_name','entity','activity_type','quarter','month','periodicals','narations','due_date','target_date','actual_completion_date','event_modified','status','assign_to']
    list_editable = ['target_date','actual_date','remarks']

    # list_per_page = 20 # No of records per page 
    list_display = [
        'entity',
        'activity_name',
        'activity_type',
        'quarter',
        'due_date',
        'target_date',
        'actual_date',
        'status',
        'assign_to',
        'remarks',
        'is_edited'
        ]


    def days(self, obj):
        # today = datetime.date.today()
        delayed =  datetime.date.today() -  obj.due_date
        delayed=delayed.days
        return str(delayed) +  " " + "days"
        # if today > obj.due_date:
        #     diff = today - obj.due_date
        #     return str(diff.days) +" "+ "days"
        # else:
        #     return "On-Time"

    

    def has_module_permission(self, request, obj=None):
        return True

    # def has_add_permission(self, request):
    #     return True

    def has_add_permission(self, request):
        # if request.user.is_staff and not request.user.is_superuser:
        #     return False
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        if request.user.is_staff and not request.user.is_superuser:
            self.list_editable = []
        else:
            self.list_editable = ['target_date','actual_date','remarks', 'is_edited']
            
    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser:
            activity = ActivityTracker.objects.filter(assign_to__id=request.user.pk)
            return activity
        else:
            activity = ActivityTracker.objects.all()
            return activity


    def get_list_display(self, request):
         default_list_display = super(ActivityTrackerAdmin, self).get_list_display(request)
         if request.user.is_superuser:
             default_list_display = ['entity', 'activity_name', 'activity_type', 'quarter', 'due_date',
                                    'target_date', 'actual_date', 'days','status', 'assign_to', 'remarks', 'is_edited']
         else:
             default_list_display = ['entity', 'activity_name', 'activity_type', 'quarter', 'due_date',
                                    'target_date', 'actual_date', 'days', 'status', 'assign_to', 'remarks']
         return default_list_display

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if request.user.is_staff and not request.user.is_superuser:
            if obj and obj.is_edited == True:
                context.update({
                    # 'show_save': False,
                    'show_save_and_continue': False,
                    'show_delete': False,
                    'show_save_and_add_another':False
                })
            else:
                context.update({
                    'show_save_and_continue': False,
                    'show_delete': False,
                    'show_save_and_add_another':False
                })
        return super().render_change_form(request, context, add, change, form_url, obj)


    def get_form(self, request, obj=None, **kwargs):
        """Remove restaurant owner field if a user is a restaurant owner. 
        """
        form = super().get_form(request, obj, **kwargs)
        if request.user.is_staff and not request.user.is_superuser:
            self.exclude = ('assign_to', 'is_edited',)
            if obj and obj.is_edited == True:
                self.readonly_fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'month', 'due_date', 
                                    'periodicals', 'narations', 'actual_date', 'status',)
                self.fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'month', 'due_date', 
                                    'periodicals', 'narations', 'target_date','actual_date','remarks')
                messages.add_message(request, messages.ERROR, 'You need to ask Admin for permission ')
            else:
                self.readonly_fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'month', 'due_date', 
                                    'periodicals', 'narations',)
                self.fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'month', 'due_date', 
                                        'periodicals', 'narations', 'target_date','actual_date','remarks')
        elif request.user.is_superuser:
            self.readonly_fields = ()
            self.exclude = ()
        return super(ActivityTrackerAdmin, self).get_form(request, obj=None, **kwargs)
    

    def save_model(self, request, obj, form, change):
        """Save current login user id for the restaurant owner.
        """
        if request.user.is_staff and not request.user.is_superuser:
            if not obj.is_edited:
                obj.is_edited = True
                obj.save()
        super(ActivityTrackerAdmin, self).save_model(request, obj, form, change)
    
    # def get_import_formats(self):
    #     """
    #     Return available import formats.
    #     """
    #     formats = DEFAULT_FORMATS[:1]
    #     return [f for f in formats if f().can_import()]

    # def get_export_formats(self):
    #     """
    #     Return available import formats.
    #     """
    #     formats = DEFAULT_FORMATS[:1]
    #     return [f for f in formats if f().can_export()]
    # pass
    
    def save_model(self, request, obj, form, change):
        if request.user.is_staff and not request.user.is_superuser:
            if not obj.is_edited and obj._loaded_values['actual_date'] != obj.actual_date:
                obj.is_edited = True
                obj.save()
        super(ActivityTrackerAdmin, self).save_model(request, obj, form, change)


admin.site.site_header = "Finance Activity Tracker"
admin.site.site_title  =  "Finance Activity Tracker"
admin.site.index_title  =  "Finance Activity Tracker Admin"