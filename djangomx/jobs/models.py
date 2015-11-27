# coding: utf-8
import os
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify

from core.utils import get_filename


def get_upload_to(instance, filename):
    name, ext = os.path.splitext(filename)
    return 'jobs-images/%s' % get_filename(ext)


class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField(max_length=800)
    contact = models.EmailField()

    active = models.BooleanField(default=True)
    aproved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Oferta de trabajo'
        verbose_name_plural = u"Ofertas de trabajo"
        ordering = ["-created_at"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = '%s-%s' % (
            datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), slugify(self.title)
        )
        super(Job, self).save(*args, **kwargs)
