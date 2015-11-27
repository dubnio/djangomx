# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='content',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(unique=True, max_length=200),
        ),
    ]
