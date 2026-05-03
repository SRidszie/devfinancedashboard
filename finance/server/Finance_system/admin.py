from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export import resources
from django.utils.translation import gettext as _
from django.contrib import messages
# Register your models here.
from .models import *
from import_export.signals import post_import, post_export
import json
from import_export.widgets import ForeignKeyWidget
import datetime
from user.models import User
# @admin.register(User)
# class CustomUserAdmin(admin.ModelAdmin):
    
#     def save_model(self, request, obj, form, change):
#         # Override this to set the password to the value in the field if it's
#         obj.set_password(obj.password)
#         obj.save()


@admin.register(EnityName)
class EnityNameAdmin(ImportExportModelAdmin):
    list_filter = ['entity_name',]
    list_per_page = 7 # No of records per page 

    def has_module_permission(self, request, obj=None):
        print("~~~~~~~~~~~~~~~~~~~>")
        print("user", getattr(request.user, "is_sub_admin", False))
        print("~~~~~~~~~~~~~~~~~~~>")
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False
        elif request.user.is_staff and not request.user.is_superuser and getattr(request.user, "is_sub_admin", False):
            self.list_filter = ['entity_name',]
            return False

    def has_add_permission(self, request):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff and request.user.is_superuser:
            return True
        elif request.user.is_staff and not request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return False

@admin.register(ActivityName)
class ActivityNameAdmin(ImportExportModelAdmin):
    list_filter = ['name',]
    list_per_page = 7 # No of records per page
    def has_module_permission(self, request, obj=None):
        print("~~~~~~~~~~~~~~~~~~~>")
        print("user", getattr(request.user, "is_sub_admin", False))
        print("~~~~~~~~~~~~~~~~~~~>")
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False
        elif request.user.is_staff and not request.user.is_superuser and getattr(request.user, "is_sub_admin", False):
            self.list_filter = ['name',]
            return False

    def has_add_permission(self, request):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff and request.user.is_superuser:
            return True
        elif request.user.is_staff and not request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return False
@admin.register(ActivityType)
class ActivityTypeAdmin(ImportExportModelAdmin):
    list_filter = ['type',]
    list_per_page = 7
    def has_module_permission(self, request, obj=None):
        print("~~~~~~~~~~~~~~~~~~~>")
        print("user", getattr(request.user, "is_sub_admin", False))
        print("~~~~~~~~~~~~~~~~~~~>")
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False
        elif request.user.is_staff and not request.user.is_superuser and getattr(request.user, "is_sub_admin", False):
            self.list_filter = ['type',]
            return False

    def has_add_permission(self, request):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff and request.user.is_superuser:
            return True
        elif request.user.is_staff and not request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return False
class ActivityTrackerResource(resources.ModelResource):
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
        model = ActivityTracker
        report_skipped = True
        skip_unchanged = False
        exclude = ('id',)
        import_id_fields = ('entity',)
        

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


    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            activity = ActivityTracker.objects.filter(assign_to__id=request.user.pk)
            return activity
        elif request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            restaurants = ActivityTracker.objects.all()
            return restaurants

    # def delayed_by(self, obj):
    #     today = datetime.date.today()
    #     if today > obj.due_date:
    #         diff = today - obj.due_date
    #         return str(diff.days) +" "+ "days"
    #     else:
    #         return "On-Time"

    # delayed_by.short_description = 'Delayed By'

    def has_module_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        if request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False
        elif request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        if request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            self.list_editable = []
        elif request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            self.list_editable = ['target_date','actual_date','remarks', 'is_edited']
            
    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff and request.user.is_superuser:
            return True
        elif request.user.is_staff and not request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return False

    def get_list_display(self, request):
         default_list_display = super(ActivityTrackerAdmin, self).get_list_display(request)
         if request.user.is_superuser and getattr(request.user, "is_sub_admin", False):
             default_list_display = ['entity', 'activity_name', 'activity_type', 'quarter', 'due_date',
                                    'target_date', 'actual_date', 'days','status', 'assign_to', 'remarks', 'is_edited']
         else:
             default_list_display = ['entity', 'activity_name', 'activity_type', 'quarter', 'due_date',
                                    'target_date', 'actual_date', 'days', 'status', 'assign_to', 'remarks']
         return default_list_display

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            if obj.is_edited == True:
                context.update({
                    'show_save': True,
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

        if request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            self.exclude = ('assign_to', 'is_edited',)
            if obj.is_edited == True:
                self.readonly_fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'month', 'due_date', 
                                    'periodicals', 'narations', 'actual_date', 'status',)
                self.fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'month', 'due_date', 
                                    'periodicals', 'narations', 'target_date','actual_date','remarks')
                messages.add_message(request, messages.ERROR, 'You need to ask admin for access!')
            else:
                self.readonly_fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'month', 'due_date', 
                                    'periodicals', 'narations')
                self.fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'month', 'due_date', 
                                        'periodicals', 'narations', 'target_date','actual_date','remarks')
        elif request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            self.fields = ('entity', 'activity_name', 'activity_type', 'quarter', 'due_date',
                                   'periodicals', 'narations','periodicals', 'narations', 'target_date', 'actual_date', 'assign_to', 'remarks')
            self.readonly_fields = ()
            self.exclude = ()
        return super(ActivityTrackerAdmin, self).get_form(request, obj=None, **kwargs)
    

    def save_model(self, request, obj, form, change):
        if request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            if not obj.is_edited and obj._loaded_values['actual_date'] != obj.actual_date:
                obj.is_edited = True
                obj.save()

        super(ActivityTrackerAdmin, self).save_model(request, obj, form, change)


admin.site.site_header = "Finance Activity Tracker"
admin.site.site_title  =  "Finance Activity Tracker"
admin.site.index_title  =  "Finance Activity Tracker Admin"