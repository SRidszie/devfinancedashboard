import imp
from re import I
from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.db.models import Q


admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    
    def has_module_permission(self, request, obj=None):
        print("~~~~~~~~~~~~~~~~~~~>")
        print("user", getattr(request.user, "is_sub_admin", False))
        print("~~~~~~~~~~~~~~~~~~~>")
        if request.user.is_staff and request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_add_permission(self, request):
        if request.user.is_staff and request.user.is_superuser:
            return True
        elif request.user.is_staff and not request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_staff and request.user.is_superuser:
            return True
        elif request.user.is_staff and not request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_staff and request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return True
        elif request.user.is_staff and not request.user.is_superuser and not getattr(request.user, "is_sub_admin", False):
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_staff and request.user.is_superuser:
            return True
        elif request.user.is_staff and not request.user.is_superuser or getattr(request.user, "is_sub_admin", False):
            return False

    def save_model(self, request, obj, form, change):
        # Override this to set the password to the value in the field if it's
        obj.set_password(obj.password)
        obj.save()
