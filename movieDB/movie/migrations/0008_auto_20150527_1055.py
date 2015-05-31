# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20150527_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='film',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='film',
            name='language',
        ),
        migrations.DeleteModel(
            name='Film',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 27, 10, 55, 53, 307799)),
        ),
    ]
