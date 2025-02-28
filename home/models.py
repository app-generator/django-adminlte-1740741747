# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Devicetype(models.Model):

    #__Devicetype_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Devicetype_FIELDS__END

    class Meta:
        verbose_name        = _("Devicetype")
        verbose_name_plural = _("Devicetype")


class Devicestatus(models.Model):

    #__Devicestatus_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    is_available = models.BooleanField()
    fault_level = models.IntegerField(null=True, blank=True)

    #__Devicestatus_FIELDS__END

    class Meta:
        verbose_name        = _("Devicestatus")
        verbose_name_plural = _("Devicestatus")


class Device(models.Model):

    #__Device_FIELDS__
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    warranty_end = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.ForeignKey(DeviceStatus, on_delete=models.CASCADE)

    #__Device_FIELDS__END

    class Meta:
        verbose_name        = _("Device")
        verbose_name_plural = _("Device")


class Devicestatuslog(models.Model):

    #__Devicestatuslog_FIELDS__
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    status = models.ForeignKey(DeviceStatus, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    reason = models.TextField(max_length=255, null=True, blank=True)

    #__Devicestatuslog_FIELDS__END

    class Meta:
        verbose_name        = _("Devicestatuslog")
        verbose_name_plural = _("Devicestatuslog")



#__MODELS__END
