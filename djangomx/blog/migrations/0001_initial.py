# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations

from tinymce import models as tinymcemodels

from core import utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=' ', max_length=255, verbose_name='T\xedtulo')),
                ('slug', models.SlugField(help_text='Identificador Uri', unique=True, max_length=255, verbose_name='Slug')),
                ('description', models.CharField(help_text=' ', max_length=255, verbose_name='Descripci\xf3n', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categor\xeda',
                'verbose_name_plural': 'Categor\xedas',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=' ', max_length=255, verbose_name='T\xedtulo')),
                ('slug', models.SlugField(help_text='Identificador Uri', unique=True, max_length=255, verbose_name='Slug')),
                ('image', models.ImageField(help_text='Imagen destacada', upload_to=utils.generate_filepath('blog'), verbose_name='Im\xe1gen', blank=True)),
                ('content', tinymcemodels.HTMLField()),
                ('extract', tinymcemodels.HTMLField(blank=True)),
                ('published_at', models.DateTimeField(verbose_name='Fecha de publicaci\xf3n')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Likes')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(verbose_name='Autor', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='Categor\xeda', blank=True, to='blog.Category', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Posts',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
