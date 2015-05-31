# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20150527_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='meta_score',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 27, 10, 55, 31, 719834)),
        ),
    ]
