from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django import forms
from django.forms import ClearableFileInput
from django.contrib.auth.models import User

# for deleting media files after record is deleted
from django.db.models.signals import post_delete
from django.dispatch import receiver


from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class EnityName(models.Model):
        # fields of the model
    # entity_code = models.CharField(max_length = 255)
    entity_name = models.CharField(max_length = 255)
    last_modified = models.DateTimeField(auto_now_add = True)
 
        # renames the instances of the model
    def __str__(self):
        return self.entity_name

    class Meta:
        verbose_name = "EnityName"
        verbose_name_plural = "Entity Name"


class ActivityName(models.Model):
        # fields of the model
    name = models.CharField(max_length = 255)
    last_modified = models.DateTimeField(auto_now_add = True)
 
        # renames the instances of the model
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ActivityName"
        verbose_name_plural = "Activity Name"

class ActivityType(models.Model):
        # fields of the model
    type = models.CharField(max_length = 255)
    last_modified = models.DateTimeField(auto_now_add = True)
 
        # renames the instances of the model
    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name = "ActivityType"
        verbose_name_plural = "Activity Type"


class ActivityTracker(models.Model):

    STATUS_CHOICES = (
        ("On_Time", 'On-Time'),
        ("Delayed", 'Delayed'),
        ("Pending", 'Pending'),
    )

    Q_choice = (
        ("Q1", 'Q1'),
        ("Q2", 'Q2'),
        ("Q3", 'Q3'),
        ("Q4", 'Q4'),
    )

    month_choice = (
        ("1", 'Jan.'),
        ("2", 'Feb.'),
        ("3", 'Mar.'),
        ("4", 'Apr.'),
        ("5", 'May'),
        ("6", 'Jun.'),
        ("7", 'Jul.'),
        ("8", 'Aug.'),
        ("9", 'Sep.'),
        ("10", 'Oct.'),
        ("11", 'Nov.'),
        ("12", 'Dec.'),

    )
        # fields of the model
    # entity =  models.CharField(max_length=255)
    entity = models.ForeignKey('EnityName',default = 1,on_delete=models.CASCADE)
    activity_name = models.ForeignKey('ActivityName', default = 1,on_delete=models.CASCADE)
    # activity_name =  models.CharField(max_length=255)
    # activity_type =  models.CharField(max_length=255)
    activity_type = models.ForeignKey('ActivityType', default = 1,on_delete=models.CASCADE)
    # year = models.DateTimeField(null=True, blank=True)
    quarter = models.CharField(max_length=255, default = 1,choices = Q_choice)
    month = models.CharField(max_length=255, default = 1,choices = month_choice)
    periodicals = models.TextField(blank=True)
    narations= models.TextField(blank=True)
    due_date = models.DateField()
    target_date = models.DateField(blank=True,null=True)
    actual_date = models.DateField(blank=True,null=True)
    event_modified = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=255,editable=False,default = 1 )
    # assign_to = models.ForeignKey(User, on_delete=models.CASCADE,default = 1)
    assign_to = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default = 1)
    remarks = models.CharField(max_length=255,blank=True)
    is_edited = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if self.actual_date:
            if self.actual_date <= self.due_date:
                self.status = 'On-Time'
            elif self.actual_date > self.due_date:
                self.status = 'Delayed'
            else:
                self.status = 'Pending'
        else:
            self.status='Pending'
        return super().save(*args,**kwargs)

 
        # renames the instances of the model
    def __str__(self):
        return str(self.activity_name) 

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        # save original values, when model is loaded from database,
        instance._loaded_values = dict(zip(field_names, values))
        return instance
    
    class Meta:
        verbose_name = "ActivityTracker"
        verbose_name_plural = "Activity Tracker Dashboard"



