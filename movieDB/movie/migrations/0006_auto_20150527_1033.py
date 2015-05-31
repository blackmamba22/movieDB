# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20150526_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_entered',
            field=models.DateTimeField(default=datetime.date(2015, 5, 27)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 27, 10, 33, 0, 411321)),
        ),
    ]
