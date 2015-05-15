# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20150509_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(help_text=b'release year', null=True),
        ),
    ]
