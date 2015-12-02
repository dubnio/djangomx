# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='extract',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_at',
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Descripci\xf3n', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Identificador URI', unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, verbose_name='T\xedtulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, to='blog.Category', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='Imagen destacada', upload_to=b'blog/<function get_upload_to at 0x10f69a9b0>', verbose_name='Imagen', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Identificador URI', unique=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=75, verbose_name='T\xedtulo'),
        ),
    ]
