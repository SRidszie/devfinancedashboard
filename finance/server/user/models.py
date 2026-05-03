from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=True, is_active=True, is_superuser=False)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        u = self.create_user(username, email, password)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.is_sub_admin = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    emp_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    reporting_manager_name = models.CharField(max_length=255)
    reporting_manager_email1 = models.EmailField()
    reporting_manager_email2 = models.EmailField()
    ceo_email = models.EmailField()
    is_sub_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, module):
        return self.is_superuser
