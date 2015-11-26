# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='photosize',
            name='by_max_side',
            field=models.BooleanField(default=False, help_text='If selected the image will be scaled to the max side', verbose_name='use max side?'),
        ),
    ]
