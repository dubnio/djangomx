# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151130_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='T\xedtulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(related_name='post', verbose_name='Autor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(related_name='post', blank=True, to='blog.Category', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='Imagen destacada', upload_to=b'blog/<function get_upload_to at 0x1093259b0>', verbose_name='Imagen', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, max_length=75, editable=False),
        ),
    ]
