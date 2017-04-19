# coding: utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Subscription(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    activation_code = models.CharField(max_length=40, blank=True, null=True)
    subscribed = models.BooleanField(default=True)
    subscribe_date = models.DateTimeField(blank=True, null=True)
    unsubscribed = models.BooleanField(default=False)
    unsubscribe_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.email)
