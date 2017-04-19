# coding: utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.core.urlresolvers import reverse
from django.db import models

from core.models import TimeStamppedModel
from core.utils import truncated_slugify

@python_2_unicode_compatible
class Job(TimeStamppedModel):
    title = models.CharField(max_length=75)
    slug = models.SlugField(unique=True, max_length=75)
    content = models.TextField(max_length=500)
    contact = models.EmailField()

    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Oferta de trabajo'
        verbose_name_plural = u"Ofertas de trabajo"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = truncated_slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
            'year': self.created_at.year,
            'month': self.created_at.month,
            'day': self.created_at.day,
            'slug': self.slug,
        }
        return reverse('jobs:job_detail', kwargs=kwargs)
