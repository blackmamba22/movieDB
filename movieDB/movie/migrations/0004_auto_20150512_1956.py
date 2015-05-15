# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20150512_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='file_path',
            field=models.CharField(max_length=255, null=True, editable=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(to='movie.MovieGenre', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.IntegerField(help_text=b'length (in minutes)', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='raw_name',
            field=models.CharField(max_length=128, null=True, editable=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(help_text=b'movie title', max_length=128, null=True),
        ),
    ]
