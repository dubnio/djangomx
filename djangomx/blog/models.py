# coding: utf-8
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from core.models import TimeStamppedModel
from core.utils import generate_filepath, truncated_slugify

from .managers import PostManager


class Category(TimeStamppedModel):
    """ A categories to add to posts. """
    title = models.CharField(verbose_name=_(u'Título'), max_length=50)
    slug = models.SlugField(editable=False, max_length=50, unique=True)
    description = models.CharField(verbose_name=_(u'Descripción'), max_length=255, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorías')

    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        self.slug = truncated_slugify(self.title, 50)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'category_slug': self.slug})


class Post(TimeStamppedModel):
    """ A blog post. """
    title = models.CharField(verbose_name=_(u'Título'), max_length=75)
    slug = models.SlugField(editable=False, max_length=75, unique=True)
    description = models.TextField(blank=True, null=True, help_text=u'Descripción usada para SEO')
    image = models.ImageField(verbose_name=_(u'Imagen'), help_text=_(u'Imagen destacada'), blank=True, upload_to=generate_filepath('blog'))
    content = models.TextField(help_text=_(u'Este es el contenido de el Post'))
    category = models.ForeignKey(Category, null=True, blank=True, related_name='post')
    author = models.ForeignKey(User, verbose_name=_(u'Autor'), related_name='post')
    likes = models.PositiveIntegerField(verbose_name=_(u'Likes'), default=0)

    is_active = models.BooleanField(default=True)

    objects = PostManager()

    class Meta:
        ordering = ["-created_at"]

    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        self.slug = truncated_slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        kwargs = {
            'year': self.created_at.year,
            'month': self.created_at.month,
            'day': self.created_at.day,
            'slug': self.slug,
        }
        return reverse('blog:view_post', kwargs=kwargs)

    @property
    def full_url(self):
        current_site = Site.objects.get_current()
        return '{}{}'.format(current_site.domain, self.get_absolute_url())

    @property
    def img_full_url(self):
        if self.image:
            current_site = Site.objects.get_current()
            return '{}{}'.format(current_site.domain, self.image.url)
        return ''
