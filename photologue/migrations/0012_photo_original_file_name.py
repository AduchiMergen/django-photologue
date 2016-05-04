# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='original_file_name',
            field=models.CharField(max_length=1000, verbose_name='original file name', blank=True),
        ),
    ]
