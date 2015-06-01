# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(default=b'Pangea', help_text=b'Country Name', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Blank', help_text=b'Director Name', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Blank', help_text=b'film title', max_length=128)),
                ('year', models.CharField(help_text=b'release year', max_length=15, null=True, blank=True)),
                ('type', models.CharField(default=b'filmdb', help_text=b'series, filmdb', max_length=20)),
                ('award', models.CharField(default=b'Blank', max_length=128, null=True, help_text=b'film awards')),
                ('plot', models.TextField(help_text=b'Film plot', max_length=256, null=True, blank=True)),
                ('poster', models.CharField(help_text=b'link to poster image', max_length=256, null=True, blank=True)),
                ('released', models.CharField(default=b'Blank', help_text=b'release date', max_length=128)),
                ('runtime', models.CharField(default=b'Blank', help_text=b'film length', max_length=15)),
                ('imdb_id', models.CharField(default=1, max_length=15, null=True, blank=True)),
                ('rated', models.CharField(default=1, max_length=15, null=True, blank=True)),
                ('meta_score', models.CharField(max_length=10, null=True, blank=True)),
                ('actor', models.ManyToManyField(to='filmdb.Actor', verbose_name=b'Actor/Actress', blank=True)),
                ('country', models.ManyToManyField(default=1, to='filmdb.Country', blank=True)),
                ('director', models.ForeignKey(default=1, to='filmdb.Director')),
                ('genre', models.ForeignKey(default=1, to='filmdb.MovieGenre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_name', models.CharField(default=b'Blank', help_text=b'Language', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ManyToManyField(to='filmdb.Language'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='filmdb',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 27, 10, 57, 41, 365691)),
        ),
    ]
